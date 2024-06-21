class Movemaster:
    def nesting(self):
        print("NST")

    def origin(self):
        print("OG")

    def write_hand(self):
        print("WH")
        print("<answerY")

    def write_mem(self):
        print("DR")
        print("<answer>")

    def set_speed(self):
        print("SP <0-9> <H or L>")  # H is faster brake, accelerate than L


robot = Movemaster()

if __name__ == "__main__":
    while 1337:
        try:
            exec(input(">>>"))
        except NameError:
            print("Wrong name")
