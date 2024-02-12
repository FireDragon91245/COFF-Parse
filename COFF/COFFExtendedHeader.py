from Common import bytes_to_int


class COFFExtendedHeader:
    SIZE = 28

    def __init__(self, litle_endian, bytes):
        self.bytes = bytes
        self.litle_endian = litle_endian
        self.magic = bytes_to_int(bytes[0:1], litle_endian)
        self.vstamp = bytes_to_int(bytes[2:3], litle_endian)
        self.tsize = bytes_to_int(bytes[4:7], litle_endian)
        self.dsize = bytes_to_int(bytes[8:11], litle_endian)
        self.bsize = bytes_to_int(bytes[12:15], litle_endian)
        self.entry = bytes_to_int(bytes[16:19], litle_endian)
        self.text_start = bytes_to_int(bytes[20:23], litle_endian)
        self.data_start = bytes_to_int(bytes[24:27], litle_endian)

    def __str__(self):
        return f'Magic: {self.magic}\n' \
               f'Version Stamp: {self.vstamp}\n' \
               f'Text Size: {self.tsize}\n' \
               f'Data Size: {self.dsize}\n' \
               f'BSS Size: {self.bsize}\n' \
               f'Entry Point: {self.entry}\n' \
               f'Text Start: {self.text_start}\n' \
               f'Data Start: {self.data_start}\n'
