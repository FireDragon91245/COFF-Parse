from enum import Flag, auto


class COFFExtendedHeaderFlags(Flag):
    """
    Note that these flags do mean different things depending on the COFFExtendedHeaderMagic value (PE32 or PE32_PLUS)
    """
    EXTENDED_HEADER_STANDARD = auto()  # Standard fields that are present in all COFF implementations if the extended header is present
    EXTENDED_HEADER_WINDOWS_SPECIFIC = auto()  # Windows specific fields that are not standard, provide extra information to
    EXTENDED_HEADER_WINDOWS_DATA_DIRECTORIES = auto()  # Windows specific fields that are not standard, provide extra information for images (like system images not pngs :))
