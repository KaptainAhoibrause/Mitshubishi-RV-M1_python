import socket

DEBUG = True

class commands:
    def __init__(self, host, port, timeout_s):
        if DEBUG != True:
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
        command = "INST:NSEL " + str(channel_Id) + "\n"
        if DEBUG == True:
            print(">-DEBUG MESSAGE->" + command)
        else:
            self.s.sendall(command.encode('ascii'))

    def read_selected_channel_id(self):
        """Checks which channel is selected (1/2/3/4)."""
        command = "INST:SEL?" + "\n"
        if DEBUG == True:
            print(">-DEBUG MESSAGE->" + command)
            return None
        else:
            self.s.sendall(command.encode('ascii'))
            response = self.s.recv(1024).decode('ascii')  # Liest Antwort des Gerät
            show_response(response)
            return response


    def toggle_channel(self, channel_Id):
        """Turns on the output of a specified channel."""
        # DOES NOT WORK ############################
        # command = "OUTP:STAT ?" + "\n"
        # self.s.sendall(command.encode('ascii'))
        # Liest Antwort des Gerät
        # response = self.s.recv(1024).decode('ascii')
        # self.turn_off_output()

    def turn_on_channel(self, channel_Id):
        """Turns on the output of a specified channel"""
        if commands.read_selected_channel_id(self) == channel_Id:
            pass
        else:
            commands.select_channel(self, channel_Id)
        command = "OUTP:STATe on" + "\n"
        if DEBUG == True:
            print(">-DEBUG MESSAGE->" + command)
        else:
            self.s.sendall(command.encode("ascii"))

    def turn_off_channel(self, channel_Id):
        """Turns off the output of a specified channel."""
        if commands.read_selected_channel_id(self) == channel_Id:
            pass
        else:
            commands.select_channel(self, channel_Id)
        command = "OUTP:STATe off" + "\n"
        if DEBUG == True:
            print(">-DEBUG MESSAGE->" + command)
        else:
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
