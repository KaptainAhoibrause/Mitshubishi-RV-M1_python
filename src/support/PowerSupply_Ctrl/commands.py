import socket


class commands:
    def __init__(self, host, port, timeout_s):
        self.HOST = host
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
        self.s.timeout(timeout_s)

    def query_execute(self):
        pass

    def cmd_execute(self):
        pass

    def select_channel(self, channel_Id):
        """Selects the channel to change/read its properties."""
        command = "INST:NSEL " + channel_Id + "\n"
        self.s.sendall(command.encode('ascii'))

    def read_selected_channel_id(self):
        """Checks which channel is selected (1/2/3/4)."""
        command = "INST:SEL?" + "\n"
        self.s.sendall(command.encode('ascii'))
        response = self.s.recv(1024).decode('ascii')  # Liest Antwort des Gerät
        show_response(response)

    def toggle_channel(self):
        """Turns on the output of the selected channel."""
        # DOES NOT WORK ############################
        # command = "OUTP:STAT ?" + "\n"
        # self.s.sendall(command.encode('ascii'))
        # Liest Antwort des Gerät
        # response = self.s.recv(1024).decode('ascii')
        # self.turn_off_output()

    def turn_off_channel(self):
        """Turns off the output of the selected channel."""
        command = "OUTP:STATe off" + "\n"
        self.s.sendall(command.encode('ascii'))

    # Turns on the generel output (supplies power)
    def turn_on_output(self):
        pass

    # Turns off the generel output (don't supplies power)
    def turn_off_output(self):
        pass


user = commands("192.168.100.10", 5025, 5)


def show_response(str):
    print(str)
