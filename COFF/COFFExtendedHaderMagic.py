from enum import Enum


class COFFExtendedHeaderMagic(Enum):
    PE32 = 0x10b
    PE32_PLUS = 0x20b
