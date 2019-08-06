import datetime
import hashlib
import sys

import pytz

from Flask_Projects.bluetooth_reader import constants

""" <summary>
 /// Brivo Shake128 strategy as part of protocol v1.
 /// We can create more of these strategies for future iterations of the
 protocol and inject as appropriate.
 /// </summary>"""


class BrivoShake128Strategy:

    ProtocolVersion = b'01'
    credentialByteLength = 208 / int(constants.BitsPerByte)
    shake128ByteLength = 128 / int(constants.BitsPerByte)

    @staticmethod
    def round_time(dt=None, round_to=30):
        if dt is None:
            dt = datetime.datetime.now()
        seconds = (dt - dt.min).seconds
        rounding = seconds - (seconds % round_to)  # Rounds down
        # rounding = (seconds+round_to/2) // round_to * round_to  # will round up
        return dt + datetime.timedelta(0, rounding-seconds, -dt.microsecond)

    def TransmissionPacket(self, user_id, door_id, credential, time_frame=30):
        # Establish all key values
        userIdBytes = bytes("%08x" % (user_id), "UTF-8")
        doorIdBytes = bytes("%08x" % (door_id), "UTF-8")
        currentTime = datetime.datetime.utcnow()
        # currentTime = datetime.datetime(2017,11,10,20,53,59)
        flooredTime = self.round_time(currentTime, time_frame)
        flooredTime = pytz.utc.localize(flooredTime)
        flooredTimeString = flooredTime.strftime("%Y-%m-%dT%H:%M:%SZ")  # this hard codes the 'Z' into the string. Brivo probably has a typo. if they fix it. this may have to be a '%Z'
        credentialShakeBytes = self.shake128("{}:{}:{}".format(flooredTimeString, credential, door_id))

        # Create and fill out the array to be returned
        my_bytes = bytearray()
        my_bytes += self.ProtocolVersion
        my_bytes += b'00'
        my_bytes += userIdBytes
        my_bytes += doorIdBytes
        my_bytes += credentialShakeBytes
        return my_bytes

    def shake128(self, input):
        input_bytes = input.encode("utf-8")
        shake = hashlib.shake_128()
        shake.update(input_bytes)
        result = shake.hexdigest(int(self.shake128ByteLength))
        return bytearray(result, "UTF-8")
