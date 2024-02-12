from Common import bytes_to_int


class COFFHeader:

    SIZE = 20

    def __init__(self, litle_endian, bytes):
        self.bytes = bytes
        self.litle_endian = litle_endian
        self.magic = bytes_to_int(bytes[0:1], litle_endian)
        self.number_of_sections = bytes_to_int(bytes[2:3], litle_endian)
        self.time_date_stamp = bytes_to_int(bytes[4:7], litle_endian)
        self.pointer_to_symbol_table = bytes_to_int(bytes[8:11], litle_endian)
        self.number_of_symbols = bytes_to_int(bytes[12:15], litle_endian)
        self.size_of_optional_header = bytes_to_int(bytes[16:17], litle_endian)
        self.characteristics = bytes_to_int(bytes[18:19], litle_endian)

    def __str__(self):
        return f'Magic: {self.magic}\n' \
               f'Number of Sections: {self.number_of_sections}\n' \
               f'Time Date Stamp: {self.time_date_stamp}\n' \
               f'Pointer to Symbol Table: {self.pointer_to_symbol_table}\n' \
               f'Number of Symbols: {self.number_of_symbols}\n' \
               f'Size of Optional Header: {self.size_of_optional_header}\n' \
               f'Characteristics: {self.characteristics}\n'

