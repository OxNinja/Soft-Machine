from softmachine.models.stack import Stack
from softmachine.models.registers import Registers
from softmachine.models.instructions import *

class VM:
    def __init__(self):
        self.stack = Stack()
        self.regs = Registers()

    def exec(self, code):
        # parse code and exec instructions accordingly
        # for the moment 1 line per instruction 
        opcodes = [x.strip() for x in code.split("\n")]
        print(opcodes)

        for i in range(len(opcodes)):
            opcode = int(opcodes[i], 16)
            if opcode > 0 or opcode <= 0xffffffff:
                self.emulate(opcode)
            else:
                print(f"Error executing opcode #{i} ({hex(opcode)})")

    def emulate(self, opcode):
        pass
