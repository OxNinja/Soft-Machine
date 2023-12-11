from softmachine.models.stack import Stack
from softmachine.models.registers import Registers
from softmachine.models.instructions import INSTRUCTIONS

class VM:
    def __init__(self):
        self.stack = Stack()
        self.regs = Registers()
        self.opcode_size = 8

    def __repr__(self):
        data = f"""===== VM =====
{self.regs}
-----
{self.stack}"""

        return data

    def exec(self, code):
        # parse code and exec instructions accordingly
        # for the moment 1 line per instruction 
        opcodes = [x.strip() for x in code.split("\n")]

        for i in range(len(opcodes)):
            opcode = int(opcodes[i], 16)
            if opcode > 0 and opcode <= (16 ** self.opcode_size - 1):
                # get msb for instructions
                op = opcode >> (self.opcode_size - 1) * 4
                # call the correct instruction
                INSTRUCTIONS[op](self, opcode)
            else:
                print(f"Error executing opcode at offset {i} ({hex(opcode)})")
                exit(1)

        print(self)

    def stress_test(self, n):
        for x in range(n):
            INSTRUCTIONS[1](self, 0x10ffffff)
        for x in range(n):
            INSTRUCTIONS[2](self, 0x20000000)
