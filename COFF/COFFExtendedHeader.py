from COFF.COFFExtendedHaderMagic import COFFExtendedHeaderMagic
from Common import bytes_to_int


class COFFExtendedHeader:
    SIZE = 28

    @staticmethod
    def blank(self, little_endian: bool):
        return COFFExtendedHeader(little_endian)

    @staticmethod
    def from_bytes(self, little_endian: bool, bdata: bytes):
        return COFFExtendedHeader(little_endian, bdata)

    def __init__(self, litle_endian: bool, bdata: bytes | None = None):
        self._is_bdata_current = bdata is not None
        self._bdata = bdata
        self.litle_endian = litle_endian
        self.magic = COFFExtendedHeaderMagic(bytes_to_int(bdata[0:2], litle_endian))
        self.vstamp = bytes_to_int(bdata[2:4], litle_endian)
        self.tsize = bytes_to_int(bdata[4:8], litle_endian)
        self.dsize = bytes_to_int(bdata[8:12], litle_endian)
        self.bsize = bytes_to_int(bdata[12:16], litle_endian)
        self.entry = bytes_to_int(bdata[16:20], litle_endian)
        self.text_start = bytes_to_int(bdata[20:24], litle_endian)
        self.data_start = bytes_to_int(bdata[24:28], litle_endian)

    def __str__(self):
        return f'Magic: {self.magic}\n' \
               f'Version Stamp: {self.vstamp}\n' \
               f'Text Size: {self.tsize}\n' \
               f'Data Size: {self.dsize}\n' \
               f'BSS Size: {self.bsize}\n' \
               f'Entry Point: {self.entry}\n' \
               f'Text Start: {self.text_start}\n' \
               f'Data Start: {self.data_start}\n'
