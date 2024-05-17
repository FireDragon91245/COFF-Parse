from COFF.COFFHeader import COFFHeader
from COFF.COFFRelocationEntry import COFFRelocationEntry
from COFF.COFFSymbolEntry import COFFSymbolEntry
from Common import bytes_to_int, bytes_to_str


class COFFSection:
    SIZE = 40

    def __init__(self, litle_endian, bytes):
        self.bytes = bytes
        self.litle_endian = litle_endian
        if chr(bytes[0]) == '/':
            self.is_long_name = True
        else:
            self.is_long_name = False
        if not self.is_long_name:
            self.name = bytes_to_str(bytes[0:7])
        if self.is_long_name:
            self.str_table_offset = int(bytes_to_str(bytes[1:7]))
        else:
            self.str_table_offset = None
        self.paddr = bytes_to_int(bytes[8:11], litle_endian)
        self.vaddr = bytes_to_int(bytes[12:15], litle_endian)
        self.size = bytes_to_int(bytes[16:19], litle_endian)
        self.scnptr = bytes_to_int(bytes[20:23], litle_endian)
        self.relptr = bytes_to_int(bytes[24:27], litle_endian)
        self.lnnoptr = bytes_to_int(bytes[28:31], litle_endian)
        self.nreloc = bytes_to_int(bytes[32:33], litle_endian)
        self.nlnno = bytes_to_int(bytes[34:35], litle_endian)
        self.flags = bytes_to_int(bytes[36:39], litle_endian)
        self.relocation_data = []

    def __str__(self):
        return f"Is Long Name: {self.is_long_name}\n" \
               f'String Table Offset: {self.str_table_offset}\n' \
               f'Name: {self.name}\n' \
               f'Physical Address: {self.paddr}\n' \
               f'Virtual Address: {self.vaddr}\n' \
               f'Size: {self.size}\n' \
               f'Section Pointer: {self.scnptr}\n' \
               f'Relocation Pointer: {self.relptr}\n' \
               f'Line Number Pointer: {self.lnnoptr}\n' \
               f'Number of Relocations: {self.nreloc}\n' \
               f'Number of Line Numbers: {self.nlnno}\n' \
               f'Flags: {self.flags}\n'

    def get_data(self, base_offset, coff_data):
        return coff_data[self.scnptr - base_offset:self.scnptr - base_offset + self.size]

    def load_relocation_data(self, base_offset, coff_data):
        start = self.relptr - base_offset
        for i in range(self.nreloc):
            end = start + COFFRelocationEntry.SIZE
            self.relocation_data.append(COFFRelocationEntry(self.litle_endian, coff_data[start:end]))
            start = end

    def get_relocation_data(self):
        return self.relocation_data

    def load_long_name(self, base_offset, coff_data, header: COFFHeader):
        if not self.is_long_name:
            return

        start = header._pointer_to_symbol_table - base_offset + (header._number_of_symbols * COFFSymbolEntry.SIZE) + self.str_table_offset
        self.name = ''
        while chr(coff_data[start]) != '\0':
            self.name += chr(coff_data[start])
            start += 1


