import struct


class ELFHeader64:

    def __init__(self):
        self.magic_numeber = b'\x7fELF'
        self.mode = 2 # 64-bit
        self.endian = 1
        self.self_header_version = 1
        self.osabi = 0
        self.type = 2 # Executable file
        self.inst_set = 0x3e # x86_64
        self.elf_version = b'' # Unknown
        self.entry_point = None
        self.program_header_offset = None
        self.section_header_offset = None
        self.flags = 0
        self.header_size = 64
        self.program_header_size = None
        self.program_header_num = None
        self.entry_section_header_size = None
        self.entry_section_header_num = None
        self.section_header_string_table_index = None

    def assemble(self):
        header = b''
        header += self.magic_numeber
        header += bytes([self.mode])
        header += bytes([self.endian])
        header += bytes([self.self_header_version])
        header += bytes([self.osabi])
        header += b'\x00' * 8
        header += bytes([self.type])
        header += bytes([self.inst_set])
        header += self.elf_version
        header += b'\x00' * 8
        header += struct.pack('<Q', self.entry_point)
        header += struct.pack('<Q', self.program_header_offset)
        header += struct.pack('<Q', self.section_header_offset)
        header += struct.pack('<I', self.flags)
        header += struct.pack('<H', self.header_size)
        header += struct.pack('<H', self.program_header_size)
        header += struct.pack('<H', self.program_header_num)
        header += struct.pack('<H', self.entry_section_header_size)
        header += struct.pack('<H', self.entry_section_header_num)
        header += struct.pack('<H', self.section_header_string_table_index)
        return header

