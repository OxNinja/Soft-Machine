def mov(vm, opcode):
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
        
        value = vm.regs.get(index)

    elif is_reg != 0 or is_reg != 1:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    vm.regs.set(target, value)

def push(vm, opcode):
    if vm.stack.size >= vm.stack.max_size:
        print("Cannot push, the stack is full.")
        exit(1)

    # first arg can be either a register, or a value
    is_reg = opcode >> (vm.opcode_size - 2) * 4 & 0xf
    if is_reg == 0:
        value = opcode & (16 ** (vm.opcode_size - 2) - 1)
    elif is_reg == 1:
        target = opcode >> (vm.opcode_size - 3) * 4 & 0xf
        value = vm.regs.get(target)
    else:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    vm.stack.push(value)

def pop(vm, opcode):
    if vm.stack.size < 1:
        print("Cannot pop, the stack is empty.")
        exit(1)

    # first arg is always a register
    target = opcode >> (vm.opcode_size - 2) * 4 & 0xf
    if target < 0 or target >= len(vm.regs.regs):
        print(f"Unexpected value for target: {target}. Must be between 0 (included) and {len(vm.regs.regs)} (excluded).")
        exit(1)

    value = vm.stack.stack[-1]
    vm.regs.set(target, value)
    vm.stack.pop()

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
        
        value = vm.regs.get(index)

    elif is_reg != 0 or is_reg != 1:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    total = vm.regs.get(target) + value
    vm.regs.set(target, total)

def sub(vm, opcode):
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
        
        value = vm.regs.get(index)

    elif is_reg != 0 or is_reg != 1:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    total = vm.regs.get(target) - value
    vm.regs.set(target, total)

def cmp(vm, opcode):
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
        
        value = vm.regs.get(index)

    elif is_reg != 0 or is_reg != 1:
        print(f"Unexpected value for is_reg: {is_reg}. Must be either 0 or 1.")
        exit(1)

    if vm.regs.get(target) == value:
        vm.regs.set_flag_zero(True)
    else:
        vm.regs.set_flag_zero(False)

def call(vm, opcode):
    pass

def jmp(vm, opcode):
    pass

# prefixing to avoid bad behavior
def _exit(vm, opcode):
    if vm.regs.a < 0 or vm.regs.a > 232:
        print(f"Unexpected value for a: {vm.regs.a}. Must be between 0 (included) and 232 (included).")
        exit(1)
    exit(vm.regs.a)

INSTRUCTIONS = (
        mov,
        push,
        pop,
        add,
        sub,
        cmp,
        call,
        jmp,
        _exit
        )
