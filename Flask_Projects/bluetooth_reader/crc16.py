from Flask_Projects.bluetooth_reader import constants
from Flask_Projects.bluetooth_reader.constants import BitsPerNibble, BitsPerByte, ShortLsbBitmask
import crc16

class Crc:

    def calculate_crc16(self, pData, start_value=constants.Crc16StartValue):
        crc_val = start_value
        num_bytes = len(pData)
        print("num_bytes: {}".format(num_bytes))
        for i in range(0, num_bytes):
            crc_val = self.update_crc16_ccitt(crc_val, pData[i])
            print("crc_val: {}".format(crc_val))
        return crc_val

    def update_crc16_ccitt(self, crcVal, dataByte):
        dataByte = dataByte ^ (crcVal and ShortLsbBitmask)
        dataByte = dataByte ^ (dataByte << BitsPerNibble)
        updated_crc = (((dataByte << BitsPerByte) | (crcVal >> BitsPerByte)) ^ (dataByte >> BitsPerNibble) ^ (dataByte << (BitsPerNibble - 1)))
        return updated_crc

