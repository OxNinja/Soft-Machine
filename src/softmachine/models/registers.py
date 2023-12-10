class Registers:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        # only used to calculate the number of registers
        # not usable for setting the registers because Python does make a copy and not reference the original object
        self.regs = [
                self.a,
                self.b,
                self.c,
                self.d
                ]

        self.flags = 0

    def __repr__(self):
        data = "===== Registers =====\n"
        data += f"a: {self.a}\n"
        data += f"b: {self.b}\n"
        data += f"c: {self.c}\n"
        data += f"d: {self.d}\n"
        data += f"flags: {self.flags}\n"
        data += "=====           ====="
        return data
