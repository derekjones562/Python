from Flask_Projects.bluetooth_reader.constants import BitsPerNibble, BitsPerByte, ShortLsbBitmask


class Crc:

    def calculate_crc16(self, pData, numBytes, startValue):
        crc_val = startValue
        for i in range(0, numBytes):
            crc_val = self.update_crc16_ccitt(crc_val, pData[i])
        return crc_val

    def update_crc16_ccitt(self, crcVal, dataByte):
        dataByte ^= crcVal & ShortLsbBitmask
        dataByte ^= dataByte << BitsPerNibble
        updated_crc = (((dataByte << BitsPerByte) | (crcVal >> BitsPerByte)) ^ (dataByte >> BitsPerNibble) ^ (dataByte << (BitsPerNibble - 1)))
        return updated_crc
