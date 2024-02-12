from COFF.COFFExtendedHeader import COFFExtendedHeader
from COFF.COFFHeader import COFFHeader
from COFF.COFFRelocationEntry import COFFRelocationEntry
from COFF.COFFSection import COFFSection
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
        self.data = data
        self.header: COFFHeader | None = None
        self.extended_header: COFFExtendedHeader | None = None
        self.sections: list[COFFSection] | None = None
        self.symbols: list[COFFSymbolEntry] | None = None
        self.relocations: list[COFFRelocationEntry] | None = None

    def parse(self, header: bool = True, extended_header: bool = True, sections: bool = True, symbols: bool = True, relocations: bool = True):
        pass
