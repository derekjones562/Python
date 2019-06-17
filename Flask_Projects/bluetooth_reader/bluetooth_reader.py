#!/usr/bin/python
import datetime
import hashlib

from bluepy import btle
from flask import Flask, render_template, redirect, url_for, request
import requests

from Flask_Projects.bluetooth_reader.shake_128 import BrivoShake128Strategy

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
                "descriptors": []
            }
            for characteristic in service.getCharacteristics():
                readable_characteristic = {
                    "handle": characteristic.getHandle(),
                    "uuid": characteristic.uuid,
                }
                if characteristic.supportsRead():
                    readable_characteristic['read'] = characteristic.read()
                readable_characteristic['properties'] = characteristic.propertiesToString()
                readable_service['characteristics'].append(readable_characteristic)
            for descriptor in service.getDescriptors():
                readable_service['descriptors'].append(str(descriptor))

            device_services.append(readable_service)
        return device_services
    except btle.BTLEDisconnectError as disconnect:
        return None


def write_ble_device(device_addr, handle, value):
    if type(handle) == str:
        handle = int(handle)
    if handle < 1 or handle > 65535:
        return None
    while True:
        try:
            my_peripheral = btle.Peripheral(device_addr)
            my_peripheral.writeCharacteristic(handle, value.encode())
            # if my_peripheral.getCharacteristics(18)[0].supportsRead():
            #    read = my_peripheral.getCharacteristics(18)[0].read()
            #    return read
            break
        except btle.BTLEDisconnectError as disconnect:
            pass
    return None

def Hash_Credential(user_id, door, credential):
    brivo_credential = BrivoShake128Strategy().TransmissionPacket(user_id, door, credential)
    brivo_credential = bytearray(b'01020304'
                                 )
    """user_id = 254sudo 
    door = 255
    credential = "34aaab88be7b938d5d3c06c45b7d56d6997c86eb"
    date = datetime.datetime.now()
    date = datetime.date
    hashed_credential = hashlib.shake_128()
    import crc16
    crc = crc16.crc16xmodem(b'1234')
    crc = crc16.crc16xmodem(b'56789', crc)
    print(crc)
    print(hashed_credential)"""

@app.route('/')
def index():
    Hash_Credential(254, 255, "34aaab88be7b938d5d3c06c45b7d56d6997c86eb") # door_id = 22727262
    data = {}
    ble_devices = get_ble_devices()
    for device in ble_devices:
        complete_name = device.getValueText(9)
        if complete_name =='BRVO':
            data[device.addr] = complete_name
    return render_template('index.html', devices=data, **request.args)


@app.route('/device/<device_addr>', methods=['GET'])
def device_detail(device_addr):
    services = None
    while not services:
        services = get_ble_device_services(device_addr)
    return render_template('device_detail.html', services=services, device_addr=device_addr)


@app.route('/device/<device_addr>/write', methods=['GET', 'POST'])
def write_to_service(device_addr):
    read = None
    if request.method == 'POST':
        read = write_ble_device(device_addr, request.form['handle'], request.form['value'])
    handle = request.args.get('handle')
    return render_template('write_to_service.html', handle=handle, read=read)


if __name__ == '__main__':
    app.run(debug=True)
