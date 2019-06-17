import sys

from Flask_Projects.bluetooth_reader import constants
from Flask_Projects.bluetooth_reader.crc16 import Crc


class Tlv:
    def __init__(self):
        self.Value = bytearray(constants.MaxDataLen + constants.CredentialLength, "UTF-8")
        self.Tag = None
        self.Length = None
        self.Value = None
        self.TotalLength = bytes(self.Length + constants.TlvOverhead)

    def TruncatedValue(self):
        data = bytearray(self.Length + constants.TlvOverhead + constants.CredentialLength + constants.CrcLength, "UTF-8")
        data[constants.TlvTagIndex] = bytes(self.Tag)
        data[constants.TlvLengthIndex] = bytes(self.Length)
        Array.Copy(self.Value, constants.TlvTagIndex, data, constants.TlvOverhead, self.Length)
        return data

    def AppendCrc(self):
      crc = Crc().calculate_crc16(self.Value, self.Length, constants.Crc16StartValue)
      self.Value[self.Length + constants.CrcMsbIndex] = bytes((crc & constants.ShortMsbBitmask) >> constants.BitsPerByte)
      self.Value[self.Length + constants.CrcLsbIndex] = bytes(crc & constants.ShortLsbBitmask)
      self.Length += sys.getsizeof(ushort)


class Stlv(Tlv):
    def __init__(self):
        super().__init__()
        self.clear_data()
        self.Status = None
        self.Tag = None
        self.Length = None
        self.Data = None
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

    def AppendCrc(self):
        # Dev note - the CRC is reversed on the STLV from the TLV
        crc = self.CalculateCrc()
        self.Data[self.Length + constants.CrcLsbIndex] = bytes((crc & constants.ShortMsbBitmask) >> constants.BitsPerByte)
        self.Data[self.Length + constants.CrcMsbIndex] = bytes(crc & constants.ShortLsbBitmask)

    def VerifyCrc(self):
        calculatedCrc = self.CalculateCrc()
        stlvCrc = self.GetCrc()
        return calculatedCrc == stlvCrc

    def CalculateCrc(self):
        # Calculation length represents status + tag + length, and assumes data is the 4th field
        calculationLength = constants.StlvOverhead + self.Length
        return Crc().calculate_crc16(ToByteArray(), calculationLength, constants.Crc16StartValue)

    def GetCrc(self):
        crc = self.Data[self.Length + constants.CrcMsbIndex] | (self.Data[self.Length+constants.CrcLsbIndex]) << constants.BitsPerByte
        return crc

    def ToByteArray(self):
        array = bytearray(constants.MaxDataLen + constants.StlvOverhead)
        array[constants.StlvStatusIndex] = bytes(self.Status)
        array[constants.StlvTagIndex] = bytes(self.Tag)
        array[constants.StlvLengthIndex] = self.Length
        Array.Copy(self.Data, constants.StlvStatusIndex, array, constants.StlvOverhead, self.Data.Length)
        return array
