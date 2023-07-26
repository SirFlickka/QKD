keys = {}

def associate_key(ip, qkd_key):
    # Convert IP to binary.
    bin_str = ip_to_bin(ip)

    # Convert binary to hexadecimal.
    hex_str = bin_to_hex(bin_str)

    # Associate the hexadecimal string with the QKD key.
    keys[hex_str] = qkd_key
def get_key(ip):
    # Convert IP to binary.
    bin_str = ip_to_bin(ip)

    # Convert binary to hexadecimal.
    hex_str = bin_to_hex(bin_str)

    # Retrieve the QKD key.
    return keys.get(hex_str)
