# Soft Machine

Python custom virtual machine.

## Features

* [ ] Registers
    * [x] Basic registers
    * [ ] Flags
        * [x] Zero flag 
* [ ] Stack
    * [x] LIFO
    * [x] Max size 
    * [ ] Stackframes
* [ ] Heap
    * [ ] Max size
* [ ] Instructions
    * [x] `add reg, val`
    * [x] `add reg, reg`
    * [x] `sub reg, val`
    * [x] `sub reg, reg`
    * [x] `cmp reg, val`
    * [x] `cmp reg, reg`
    * [x] `mov reg, val`
    * [x] `mov reg, reg`
    * [x] `push val`
    * [x] `push reg`
    * [x] `pop reg`
    * [ ] `jmp addr`
    * [ ] `jmp label`
    * [ ] `call func`
    * [x] `exit`
* [ ] Assemble code
    * [ ] From file
    * [ ] From stdin
* [ ] Disassemble code
    * [ ] From file
    * [ ] From stdin
* [x] Exec instructions
    * [x] From file
    * [x] From stdin

## Install

```sh 
# Get sources
git clone ...
cd Soft-Machine

# Use a virtual environment
python3 -m venv my-venv
source my-venv/bin/activate

# Install via pip
pip install -e .
```

## Use

```sh
soft-machine exec -s "0x31034567;0x30001000;0x33100000;0x02110000;0x03000000;0x41120000;0x80000000"
soft-machine assemble --stdin "mov a, 11; mov b, 0x45; exit"
soft-machine disassemble --file code.bin
```
