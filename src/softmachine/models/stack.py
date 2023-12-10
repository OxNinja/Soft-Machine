class Stack:
    def __init__(self, max_size=0xffff):
        self.stack = list()
        self.max_size = max_size
        self.size = len(self.stack)

    def push(self, value):
        if self.size < self.max_size:
            self.stack.append(value)
            self.update()

    def pop(self):
        if self.size > 0:
            self.stack.pop()
            self.update()

    def update(self):
        # update size
        # we could just self.size += 1, but just to be sure
        self.size = len(self.stack)

    def __repr__(self):
        data = "===== Stack: =====\n"
        for i in range(self.size):
            data += f"{i}:\t{self.stack[i]}\n"
        data += "=====        ====="
        return data
