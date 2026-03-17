import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))

        try:
            banner = sock.recv(1024).decode().strip()
        except:
            banner = ""

        sock.close()

        return banner

    except:
        return ""
