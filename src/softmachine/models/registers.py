class Registers:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        self.regs = (
                self.a,
                self.b,
                self.c,
                self.d
                )

        self.flags = 0

    def __repr__(self):
        data = "Registers:\n"
        data += f"a: {self.a}\n"
        data += f"b: {self.b}\n"
        data += f"c: {self.c}\n"
        data += f"d: {self.d}\n"
        data += f"flags: {self.flags}"

        return data

    def get(self, index):
        # Workaround the list issue
        # as python creates a copy to the reference and not a hard link

        if index == 0:
            value = self.a
        elif index == 1:
            value = self.b
        elif index == 2:
            value = self.c
        elif index == 3:
            value = self.d

        return value

    def set(self, index, value):
        # Workaround the list issue
        # as python creates a copy to the reference and not a hard link
        
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        elif index == 2:
            self.c = value
        elif index == 3:
            self.d = value

        self.regs = (
                self.a,
                self.b,
                self.c,
                self.d
                )
