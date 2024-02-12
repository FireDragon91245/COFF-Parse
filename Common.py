def bytes_to_int(byte_array, is_little_endian):
    # Convert each byte to its hexadecimal representation
    hex_list = [f'0x{byte:02X}' for byte in byte_array]

    # Convert the byte array to integer based on endianess
    if is_little_endian:
        int_val = int.from_bytes(byte_array, 'little')
    else:
        int_val = int.from_bytes(byte_array, 'big')

    return int_val


def bytes_to_str(byte_array):
    return ''.join([chr(byte) for byte in byte_array])


def format_byte_array(bytes):
    return ' '.join([f'0x{byte:02X}' for byte in bytes])
