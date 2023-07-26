def ip_to_bin(ip):
    return ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:]
