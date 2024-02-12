from Common import bytes_to_int


class COFFRelocationEntry:
    SIZE = 10

    def __init__(self, litle_endian, bytes):
        self.bytes = bytes
        self.litle_endian = litle_endian
        self.virtual_address = bytes_to_int(bytes[0:3], litle_endian)
        self.symbol_table_index = bytes_to_int(bytes[4:5], litle_endian)
        self.type = bytes_to_int(bytes[8:9], litle_endian)

    def __str__(self):
        return f'Virtual Address: {self.virtual_address}\n' \
               f'Symbol Table Index: {self.symbol_table_index}\n' \
               f'Type: {self.type}\n'
