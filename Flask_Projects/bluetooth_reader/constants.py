MaxDataLen = 197
Crc16StartValue = b'0x6363'
StlvOverhead = b'3'
TlvOverhead = b'2'
CredentialLength = b'1'
CrcLength = b'2'
TlvTagIndex = 0
TlvLengthIndex = 1
StlvStatusIndex = 0
StlvTagIndex = 1
StlvLengthIndex = 2
CrcMsbIndex = 0
CrcLsbIndex = 1
BitsPerByte = 8
BitsPerNibble = 4
ShortMsbBitmask = b'0xFF00'
ShortLsbBitmask = b'0x00FF'

DefaultBleAuthTimeFrame = 30  # Interval that the current time is rounded to for the input into the SHAKE-128 algorithm
OkStatusResponse = b'0x00'  # Value for an OK status as part of the STLV pattern
AllowedReaders =["BRVO"]  # Brivo-branded Tri-Tech readers use “BRVO” as their name in the BLE advertisement packet
BleCredentialServiceUuid = "3420d81a-af2c-11e5-bf7ffeff819cdc9f"  # The ID of the service to discover when connecting to the reader
BleCredentialServiceReaderBytes = 8 # The length in bytes of the reader’s unique identifier
MaximumTransferUnit = 200  # The MTU used for communication between phone and reader. Developer must request MTU to be this value on the GATT connection explicitly when connecting with Android
DataTransferChrcUuid = "ee8732b3-2d52-409b-9084-70ad31f6c790"  # The ID of the characteristic to look for when connecting to the reader
ChrcUpdateNotificationDscptUuid = "00002902-0000-1000-8000-00805f9b34fb"  # The ID for the descriptor to use when receiving notifications from the reader on Android


status_ok = 0
status_fail = 1
status_bad_crc = 2
status_invalid = 3

tag_uuid = b'70'
tag_uuid_variable = b'7B'
tag_data = b'F1'
tag_data_end = b'FE'
tag_no_data = b'FF'

