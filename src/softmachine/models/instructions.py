def mov(vm, opcode):
    pass

def push(vm, opcode):
    pass

def pop(vm, opcode):
    pass

def add(vm, opcode):
    # first arg is always a register
    target = opcode >> (vm.opcode_size - 2) * 4 & 0xf
    if target < 0 or target >= len(vm.regs.regs):
        print(f"Unexpected value for target: {target}. Must be between 0 (included) and {len(vm.regs.regs)} (excluded).")
        exit(1)

    # second arg can be either a register, or a value
    is_reg = opcode >> (vm.opcode_size - 3) * 4 & 0xf

    if is_reg == 0:
        value = opcode & (16 ** (vm.opcode_size - 3) - 1)
    elif is_reg == 1:
        index = opcode >> (vm.opcode_size - 4) * 4 & 0xf
        if index < 0 or index >= len(vm.regs.regs):
            print(f"Unexpected value for index: {index}. Must be between 0 (included) and {len(vm.regs.regs)} (excluded).")
            exit(1)
        
        # not clean but Python can't update the original object that is referenced on copy in a list
        # will need fix if new registers are added to the VM
        # no switch for retro compat
        if index == 0:
            value = vm.regs.a 
        elif index == 1:
            value = vm.regs.b 
        elif index == 2:
            value = vm.regs.c 
        elif index == 3:
            value = vm.regs.d

    elif is_reg != 0 or is_reg != 1:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    # not clean but Python can't update the original object that is referenced on copy in a list
    # will need fix if new registers are added to the VM
    # no switch for retro compat
    if target == 0:
        vm.regs.a += value
    elif target == 1:
        vm.regs.b += value
    elif target == 2:
        vm.regs.c += value
    elif target == 3:
        vm.regs.d += value

def sub(vm, opcode):
    pass

def cmp(vm, opcode):
    pass

def call(vm, opcode):
    pass

def jmp(vm, opcode):
    pass

# prefixing to avoid bad behavior
def _exit(vm, opcode):
    pass

INSTRUCTIONS = [
        mov,
        push,
        pop,
        add,
        sub,
        cmp,
        call,
        jmp,
        _exit
        ]
