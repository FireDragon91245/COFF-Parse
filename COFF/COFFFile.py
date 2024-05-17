from COFF.COFFExtendedHeader import COFFExtendedHeader
from COFF.COFFHeader import COFFHeader
from COFF.COFFRelocationEntry import COFFRelocationEntry
from COFF.COFFSection import COFFSection
from COFF.COFFStringTable import COFFStringTable
from COFF.COFFSymbolEntry import COFFSymbolEntry


class COFFFile:

    @staticmethod
    def from_file(filename):
        with open(filename, 'rb') as f:
            return COFFFile(f.read())

    @staticmethod
    def from_bytes(data):
        return COFFFile(data)

    @staticmethod
    def blank():
        return COFFFile()

    def __init__(self, data=None):
        self.is_bdata_current = data is not None
        self._bdata: bytes | None = data
        self.header: COFFHeader | None = None
        self.extended_header: COFFExtendedHeader | None = None
        self.sections: list[COFFSection] | None = None
        self.symbols: list[COFFSymbolEntry] | None = None
        self.relocations: dict[int, list[COFFRelocationEntry]] | None = None
        self.string_table: COFFStringTable | None = None

    def parse(self, extended_header: bool = True, sections: bool = True, symbols: bool = True, relocations: bool = True):
        pass

    def _get_bdata(self) -> bytes:
        if not self.is_bdata_current:
            self._recalc_bdata()
        return self._bdata

    def _recalc_bdata(self):
        self.is_bdata_current = True
        self._bdata = b''
        self._bdata += self.header.byte_data
        self._bdata += self.extended_header.byte_data if self.extended_header is not None else b''

    byte_data: bytes = property(_get_bdata)

