import socket

HOST = "192.168.100.10"  # The server's hostname or IP address
PORT = 5025  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)  # Set a timeout of 5 seconds
    try:
        s.connect((HOST, PORT))
        while True:
            usrin = input(">>>") + "\n"
            s.sendall(usrin.encode('ascii'))
            try:
                data = s.recv(1024)
                print("Geräteantwort:", data.decode('ascii'))
            except socket.timeout:
                print("Timeout: Keine Antwort vom Gerät.")
    except socket.timeout:
        print("Timeout: Verbindung zum Server konnte nicht hergestellt werden.")
    except Exception as e:
        print("Ein Fehler ist aufgetreten:", e)
