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
        return COFFStringTable(endian, 0, strings)

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

    def add_string(self, string: str) -> int:
        if self._strings is None:
            self._strings = []
        self._strings.append(string)
        self._blen_current = False
        self._bdata_current = False
        return self.get_string_offset(string)

    def contains_string(self, string: str):
        return string in self._strings

    def get_string_offset(self, string: str):
        if string not in self._strings:
            return -1
        offset = 4
        for s in self._strings:
            if s == string:
                return offset
            offset += len(s) + 1
        return -1

    byte_len = property(_get_blen)
    strings = property(_get_strings)
    byte_data = property(_get_bdata)
