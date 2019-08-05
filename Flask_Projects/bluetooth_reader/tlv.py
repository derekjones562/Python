import sys

from Flask_Projects.bluetooth_reader import constants
from Flask_Projects.bluetooth_reader.crc16 import Crc


class Tlv:
    def __init__(self):
        self.value = [constants.MaxDataLen, constants.CredentialLength]
        self.tag = constants.tag_data
        self.length = 0
        self.total_length = constants.TlvOverhead + self.length

    def truncated_value(self):
        data = []
        data[constants.TlvTagIndex] = bytes(self.tag)
        data[constants.TlvLengthIndex] = bytes(self.length)
        print(data)
        data = data + self.value
        #Array.Copy(self.Value, constants.TlvTagIndex, data, constants.TlvOverhead, self.Length)
        return data

    def append_crc(self):
        crc = Crc().calculate_crc16(self.value, self.length)
        self.value[self.length + constants.CrcMsbIndex] = bytes((crc & constants.ShortMsbBitmask) >> constants.BitsPerByte)
        self.value[self.length + constants.CrcLsbIndex] = bytes(crc & constants.ShortLsbBitmask)
        self.length += sys.getsizeof(int)


class Stlv(Tlv):
    def __init__(self, status=constants.StlvStatusIndex, tag=constants.StlvTagIndex, length=constants.StlvLengthIndex):
        super().__init__()
        self.clear_data()
        self.Status = status
        self.Tag = tag
        self.Length = length
        self.Data = [constants.StlvOverhead]
        self.TransmitBytes = None

    """{
      get
      {
        # need 1 byte for status, 1 for tag, 1 for length, the this.Length for the message, and 2 for CRC
        byte[] data = new byte[self.Length + constants.StlvOverhead + constants.CrcLength]
        data[constants.StlvStatusIndex] = bytes(self.Status)
        data[constants.StlvTagIndex] = bytes(self.Tag)
        data[constants.StlvLengthIndex] = self.Length
        Array.Copy(self.Data, constants.StlvStatusIndex, data, constants.StlvOverhead, self.Length + constants.CrcLength)
        return data;
      }
      set
      {
        self.Status = (Status)value[constants.StlvStatusIndex];
        self.Tag = (Tag)value[constants.StlvTagIndex];
        self.Length = value[constants.StlvLengthIndex]
        Array.Copy(value, constants.StlvOverhead, self.Data, constants.StlvStatusIndex, self.Length + constants.CrcLength)
      }
    }"""

    def clear_data(self):
        self.Data = bytearray(constants.MaxDataLen)

    def append_crc(self):
        # Dev note - the CRC is reversed on the STLV from the TLV
        crc = self.calculate_crc()
        self.Data[self.Length + constants.CrcLsbIndex] = bytes((crc & constants.ShortMsbBitmask) >> constants.BitsPerByte)
        self.Data[self.Length + constants.CrcMsbIndex] = bytes(crc & constants.ShortLsbBitmask)

    def verify_crc(self):
        calculatedCrc = self.calculate_crc()
        stlvCrc = self.GetCrc()
        return calculatedCrc == stlvCrc

    def calculate_crc(self):
        # Calculation length represents status + tag + length, and assumes data is the 4th field
        calculationLength = constants.StlvOverhead + self.Length
        return Crc().calculate_crc16(self.to_byte_array(), calculationLength)

    def GetCrc(self):
        crc = self.Data[self.Length + constants.CrcMsbIndex] | (self.Data[self.Length+constants.CrcLsbIndex]) << constants.BitsPerByte
        return crc

    def to_byte_array(self):
        array = bytearray(constants.MaxDataLen + constants.StlvOverhead)
        array[constants.StlvStatusIndex] = bytes(self.Status)
        array[constants.StlvTagIndex] = bytes(self.Tag)
        array[constants.StlvLengthIndex] = self.Length
        # Array.Copy(self.Data, constants.StlvStatusIndex, array, constants.StlvOverhead, self.Data.Length)
        return array
