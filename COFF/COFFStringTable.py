from Common import bytes_to_int

class COFFStringTable:

    def __init__(self, little_endian: bool, blen: int, strings: list[str] = None, bdata: bytes | None = None):
        self._little_endian = little_endian
        self._strings = strings
        self._blen = blen
        self._blen_current = blen != 0
        self._bdata = bdata
        self._bdata_current = bdata is not None

    @staticmethod
    def from_bytes(little_endian: bool, data: bytes):
        return COFFStringTable(little_endian, 0, None, data)

    @staticmethod
    def from_strings(endian: bool, strings: list[str]):
        return COFFStringTable(0, strings)._recalc_blen()

    def _recalc_blen(self):
        self._blen_current = True
        self._blen = 4
        for s in self._strings:
            self._blen += len(s) + 1

    def _get_blen(self):
        if not self._blen_current:
            self._recalc_blen()
        return self._blen

    def _get_strings(self):
        return self._strings

    def _recalc_bdata(self):
        self._bdata_current = True
        self._bdata = b''
        self._bdata += self._blen.to_bytes(4, 'little' if self._little_endian else 'big')
        for s in self._strings:
            self._bdata += s.encode('utf-8') + b'\0'
        self._bdata += b'\0' * (4 - (len(self._bdata) % 4))

    def _get_bdata(self):
        if not self._bdata_current:
            self._recalc_bdata()
        return self._bdata

    byte_len = property(_get_blen)
    strings = property(_get_strings)
