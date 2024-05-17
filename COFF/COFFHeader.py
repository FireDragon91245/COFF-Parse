from COFF.COFFHeaderCharacteristics import COFFHeaderCharacteristics
from COFF.COFFHeaderMachineType import COFFHeaderMachineType
from Common import bytes_to_int, get_indian_string


class COFFHeader:

    SIZE = 20

    def __init__(self, litle_endian, bytes: bytes | None = None):
        self._is_bdata_current = bytes is not None
        self._bdata = bytes
        self._litle_endian = litle_endian
        self._machine_type: COFFHeaderMachineType = COFFHeaderMachineType(bytes_to_int(bytes[0:2], litle_endian))
        self._number_of_sections = bytes_to_int(bytes[2:4], litle_endian)
        self._time_date_stamp = bytes_to_int(bytes[4:8], litle_endian)
        self._pointer_to_symbol_table = bytes_to_int(bytes[8:12], litle_endian)
        self._number_of_symbols = bytes_to_int(bytes[12:16], litle_endian)
        self._size_of_optional_header = bytes_to_int(bytes[16:18], litle_endian)
        self._characteristics: COFFHeaderCharacteristics = COFFHeaderCharacteristics(bytes_to_int(bytes[18:20], litle_endian))

    def __str__(self):
        return f'Magic: {self._machine_type}\n' \
               f'Number of Sections: {self._number_of_sections}\n' \
               f'Time Date Stamp: {self._time_date_stamp}\n' \
               f'Pointer to Symbol Table: {self._pointer_to_symbol_table}\n' \
               f'Number of Symbols: {self._number_of_symbols}\n' \
               f'Size of Optional Header: {self._size_of_optional_header}\n' \
               f'Characteristics: {self._characteristics}\n'
    
    def _get_bdata(self) -> bytes:
        if not self._is_bdata_current:
            self._relacl_bdata()
        return self._bdata
    
    def _relacl_bdata(self):
        self._is_bdata_current = True
        endian_str = get_indian_string(self._litle_endian)
        self._bdata = b''
        self._bdata += self._machine_type.value.to_bytes(2, endian_str)
        self._bdata += self._number_of_sections.to_bytes(2, endian_str)
        self._bdata += self._time_date_stamp.to_bytes(4, endian_str)
        self._bdata += self._pointer_to_symbol_table.to_bytes(4, endian_str)
        self._bdata += self._number_of_symbols.to_bytes(4, endian_str)
        self._bdata += self._size_of_optional_header.to_bytes(2, endian_str)
        self._bdata += self._characteristics.value.to_bytes(2, endian_str)

    def _set_machine_type(self, value: COFFHeaderMachineType):
        self._machine_type = value
        self._is_bdata_current = False

    def _set_num_of_sections(self, value: int):
        self._number_of_sections = value
        self._is_bdata_current = False

    def _set_time_date_stamp(self, value: int):
        self._time_date_stamp = value
        self._is_bdata_current = False

    def _set_pointer_to_symbol_table(self, value: int):
        self._pointer_to_symbol_table = value
        self._is_bdata_current = False

    def _set_number_of_symbols(self, value: int):
        self._number_of_symbols = value
        self._is_bdata_current = False

    def _set_size_of_optional_header(self, value: int):
        self._size_of_optional_header = value
        self._is_bdata_current = False

    def _set_characteristics(self, value: COFFHeaderCharacteristics):
        self._characteristics = value
        self._is_bdata_current = False

    def add_characteristic(self, characteristic: COFFHeaderCharacteristics):
        self._characteristics |= characteristic
        self._is_bdata_current = False

    byte_data = property(lambda self: self._get_bdata())
    machine_type: COFFHeaderMachineType = property(lambda self: self._machine_type, _set_machine_type)
    number_of_sections = property(lambda self: self._number_of_sections, _set_num_of_sections)
    time_date_stamp = property(lambda self: self._time_date_stamp, _set_time_date_stamp)
    pointer_to_symbol_table = property(lambda self: self._pointer_to_symbol_table, _set_pointer_to_symbol_table)
    number_of_symbols = property(lambda self: self._number_of_symbols, _set_number_of_symbols)
    size_of_optional_header = property(lambda self: self._size_of_optional_header, _set_size_of_optional_header)
    characteristics = property(lambda self: self._characteristics, _set_characteristics)





