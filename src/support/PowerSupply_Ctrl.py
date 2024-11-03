import socket

HOST = "192.168.100.10"  # The server's hostname or IP address
PORT = 5025  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while 42:
        usrin = input(">>>")
        s.sendall(str.encode(usrin))
        data = s.recv(1024)
        print(f"Received {data!r}")
