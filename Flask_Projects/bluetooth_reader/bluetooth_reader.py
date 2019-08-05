#!/usr/bin/python
import binascii
import datetime
import hashlib

import crccheck
from bluepy import btle
from flask import Flask, render_template, redirect, url_for, request
import requests

from Flask_Projects.bluetooth_reader import constants
from Flask_Projects.bluetooth_reader.shake_128 import BrivoShake128Strategy
from Flask_Projects.bluetooth_reader.crc16 import Crc
from Flask_Projects.bluetooth_reader.tlv import Stlv

app = Flask(__name__)


class ScanDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            pass
            #print("Discovered device", dev.addr)
        elif isNewData:
            pass
            #print("Received new data from", dev.addr)


def get_ble_devices():
    my_scanner = btle.Scanner().withDelegate(ScanDelegate())
    devices = my_scanner.scan()
    my_scanner.clear()
    return devices


def get_ble_device_services(device_addr):
    try:
        device_services = []
        my_peripheral = btle.Peripheral(device_addr)
        services = my_peripheral.getServices()
        for service in services:
            readable_service = {
                "UUID": service.uuid.getCommonName(),
                "characteristics": [],
            }
            for characteristic in service.getCharacteristics():
                if characteristic.getHandle() == 18:
                    print("here")
                readable_characteristic = {
                    "handle": characteristic.getHandle(),
                    "uuid": characteristic.uuid,
                }
                if characteristic.supportsRead():
                    readable_characteristic['read'] = characteristic.read()
                readable_characteristic['properties'] = characteristic.propertiesToString()
                readable_service['characteristics'].append(readable_characteristic)
            for descriptor in service.getDescriptors():
                for characteristic in readable_service['characteristics']:
                    if characteristic['handle'] == descriptor.handle:
                        characteristic['name'] = descriptor.uuid.getCommonName()

            device_services.append(readable_service)
        return device_services
    except btle.BTLEDisconnectError as disconnect:
        return None


def write_ble_device(device_addr, handle, value):
    new_value = value
    value = ""
    for i in range(len(new_value)):
        value += new_value[i]
        if i%2 !=0:
            value += "-"
    value = value[:-1]
    """value = value.split("-")
    value.reverse()
    value = "-".join(value)"""
    print("writing_Val: {}:{}".format(type(value.encode()), value.encode()))
    if type(handle) == str:
        handle = int(handle)
    if handle < 1 or handle > 65535:
        return None
    while True:
        try:
            my_peripheral = btle.Peripheral(device_addr)
            my_peripheral.writeCharacteristic(handle, value.encode(), True)
            # if my_peripheral.getCharacteristics(18)[0].supportsRead():
            #    read = my_peripheral.getCharacteristics(18)[0].read()
            #    return read
            break
        except btle.BTLEDisconnectError as disconnect:
            pass
    return None


def get_2_character_hex(starting_int):
    return bytes("%02x" % starting_int, "UTF-8")


def crc(bytes_val):
    bytes_val = binascii.unhexlify(bytes_val)
    crc16 = crccheck.crc.CrcA().calc(bytes_val)
    return crc16


def Hash_Credential(user_id, door, credential):
    brivo_credential = BrivoShake128Strategy().TransmissionPacket(user_id, door, credential)
    brivo_credential = b'01020304'
    print(brivo_credential)

    credential_bit_length = get_2_character_hex(int(len(brivo_credential)/2)*8)
    crc_of_credential = get_2_character_hex(crc(credential_bit_length+brivo_credential))
    length_including = get_2_character_hex(int(len(credential_bit_length+brivo_credential+crc_of_credential)/2))
    length_not_including = get_2_character_hex(int(len(constants.tag_uuid_variable + length_including + credential_bit_length + brivo_credential+crc_of_credential)/2))
    overall_packet = constants.status_ok + \
                     constants.tag_data + \
                     length_not_including + \
                     constants.tag_uuid_variable + length_including + credential_bit_length + brivo_credential + crc_of_credential
    crc_of_packet = hex(crc(overall_packet))[2:].encode("UTF-8")
    stvl = overall_packet+crc_of_packet[2:]+crc_of_packet[:2]
    print("Stvl: {}".format(stvl.decode("UTF-8")))
    return stvl.decode("UTF-8")


@app.route('/')
def index():

    data = {}
    ble_devices = get_ble_devices()
    for device in ble_devices:
        complete_name = device.getValueText(9)
        if complete_name =='BRVO':
            scan_data = device.getScanData()
            for scan_data_item in scan_data:
                if scan_data_item.__contains__(33):
                    door_id = device.getValueText(33)[-8:]
                    data[device.addr] = {'name': complete_name,
                                         'scan_data': scan_data,
                                         'door_id': door_id,
                                         'rssi': device.rssi,
                                         'credential': Hash_Credential(22489071, int(door_id), "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxZWFjNmU3"),
                                         }

    return render_template('index.html', devices=data, **request.args)


@app.route('/device/<device_addr>', methods=['GET'])
def device_detail(device_addr):
    services = None
    while not services:
        services = get_ble_device_services(device_addr)
    return render_template('device_detail.html', services=services, device_addr=device_addr, door_id=request.args.get("door_id"))


@app.route('/device/<device_addr>/unlock', methods=['GET'])
def unlock_via_ble(device_addr):
    write_ble_device(device_addr, request.args.get('handle'), request.args.get('credential'))
    return redirect('/')


@app.route('/device/<device_addr>/write', methods=['GET', 'POST'])
def write_to_service(device_addr):
    read = None
    if request.method == 'POST':
        read = write_ble_device(device_addr, request.form['handle'], request.form['value'])
    handle = request.args.get('handle')
    return render_template('write_to_service.html', handle=handle, read=read)


if __name__ == '__main__':
    app.run(debug=True)
