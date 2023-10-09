import socket

def check(addr: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((addr, port))
    sock.close()
    return result == 0
    pass
