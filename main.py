import os
from pathlib import Path

from COFF.COFFSymbolEntry import COFFSymbolEntry
from Common import format_byte_array
from COFF.COFFExtendedHeader import COFFExtendedHeader
from COFF.COFFHeader import COFFHeader
from COFF.COFFSection import COFFSection


def bytes_to_hex_int(byte_array, is_little_endian):
    # Convert each byte to its hexadecimal representation
    hex_list = [f'0x{byte:02X}' for byte in byte_array]

    # Convert the byte array to integer based on endianess
    if is_little_endian:
        int_val = int.from_bytes(byte_array, 'little')
    else:
        int_val = int.from_bytes(byte_array, 'big')

    return hex_list, int_val


file_path = Path(os.path.realpath(__file__)).parent

coff_file = file_path.joinpath('hello.o')

litle_endian = True


with open(coff_file, 'rb') as f:
    coff_data = f.read()
    header = COFFHeader(litle_endian, coff_data[0:19])
    print("COFF Header")
    print(header)
    coff_data = coff_data[20:]
    if header.size_of_optional_header != 0:
        optional_header = COFFExtendedHeader(litle_endian, coff_data[0:27])
        print("COFF Extended Header")
        print(optional_header)
        coff_data = coff_data[28:]

    sections = []
    for i in range(header.number_of_sections):
        sections.append(COFFSection(litle_endian, coff_data[0:39]))
        coff_data = coff_data[40:]

    base_offset = COFFHeader.SIZE + (COFFExtendedHeader.SIZE if header.size_of_optional_header != 0 else 0) + header.number_of_sections * COFFSection.SIZE

    for i in range(header.number_of_sections):
        sections[i].load_long_name(base_offset, coff_data, header)
        print(f"Section {i + 1}")
        print(sections[i])

    for i in range(header.number_of_sections):
        section_data = sections[i].get_data(base_offset, coff_data)
        print(f"Section {i+1} Data ({sections[i].name}) (Size: {sections[i].size} bytes)")
        print(format_byte_array(section_data))

    for i in range(header.number_of_sections):
        sections[i].load_relocation_data(base_offset, coff_data)
        relocation_data = sections[i].get_relocation_data()
        print(f"Section {i+1} Relocations")
        for j, relocation in enumerate(relocation_data):
            print(f"Relocation {j+1} in for Section {i+1} ({sections[i].name})")
            print(relocation)

    for i in range(header.number_of_symbols):
        symbol = COFFSymbolEntry(litle_endian, coff_data[(header.pointer_to_symbol_table - base_offset) + COFFSymbolEntry.SIZE * i:(header.pointer_to_symbol_table - base_offset) + COFFSymbolEntry.SIZE * (i + 1)])
        symbol.load_long_name(base_offset, coff_data, header)
        print(f"Symbol {i+1}")
        print(symbol)



