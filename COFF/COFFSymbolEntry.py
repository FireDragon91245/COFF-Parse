from COFF.COFFHeader import COFFHeader
from Common import bytes_to_int, bytes_to_str


class COFFSymbolEntry:
    SIZE = 18

    def __init__(self, litle_endian, bytes):
        self.bytes = bytes
        self.litle_endian = litle_endian
        self.is_long_name = all([byte == 0 for byte in bytes[
                                                       0:2]])  # If the first 3 bytes are zero its a offset into the string table instead of the name
        if self.is_long_name:
            self.string_table_offset = bytes_to_int(bytes[4:7], litle_endian)
        else:
            self.string_table_offset = None
        self.name = bytes_to_str(bytes[0:7]) if not self.is_long_name else None
        self.value = bytes_to_int(bytes[8:11], litle_endian)
        self.section_number = bytes_to_int(bytes[12:13], litle_endian)
        self.type = bytes_to_int(bytes[14:15], litle_endian)
        self.storage_class = bytes_to_int(bytes[16:16], litle_endian)
        self.number_of_aux_symbols = bytes_to_int(bytes[17:17], litle_endian)

    def load_long_name(self, base_offset, coff_data, header: COFFHeader):
        if not self.is_long_name:
            return

        if self.string_table_offset - base_offset > len(coff_data):
            return

        start = header.pointer_to_symbol_table - base_offset + (header.number_of_symbols * COFFSymbolEntry.SIZE) + self.string_table_offset
        self.name = ''
        while chr(coff_data[start]) != '\0':
            self.name += chr(coff_data[start])
            start += 1

    def __str__(self):
        return f"Is Long Name: {self.is_long_name}\n" \
               f'String Table Offset: {self.string_table_offset}\n' \
               f'Name: {self.name}\n' \
               f'Value: {self.value}\n' \
               f'Section Number: {self.section_number}\n' \
               f'Type: {self.type}\n' \
               f'Storage Class: {self.storage_class}\n' \
               f'Number of Aux Symbols: {self.number_of_aux_symbols}\n'
