"""CPU functionality."""

import sys


LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        #Add list properties to cpu class to hold 256 bytes of memory 
        self.ram = [0] * 256
        #and 8 general purpose registers
        self.reg = [0] * 8  
        #add a program counter:
        self.pc = 0
        self.branchtable = {
            LDI: self.LDI,
            PRN: self.PRN,
            HLT: self.HLT,
            MUL: self.MUL,
            PUSH: self.PUSH,
            POP: self.POP

        }
        # self.branchtable[LDI] = self.LDI
        self.running = True
        #Stack pointer:
        #index of register that will point to stack
        # self.stack_pointer = 7
        #storing the ram index in the stack pointer
        # self.reg[7] = self.ram[0xf4]
        # self.stack_pointer = self.reg[7]
        # self.stack_pointer_index = 7
        self.reg[7] = 0xf4
        self.stack_pointer = self.reg[7]
        

    def load(self, file_name):
        """Load a program into memory."""

        # For now, we've just hardcoded a program:
        # file_name = sys.argv[1]
        with open(file_name) as f:
            address = 0

            for line in f:
                line = line.split('#')
                try:
                    v = line[0].strip()
                except ValueError:
                    continue
                if len(v) > 0:
                    self.ram[address] = int(v,2)
                    address += 1


            print('memmory', self.ram[:15])


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    #should accept the address to read and return the value stored there.
    def ram_read(self, mar):
        return self.ram[mar]

    # `ram_write()` should accept a value to write, and the address to write it to.
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr
    
    def LDI(self, registry_index, value):
        self.reg[registry_index] = value
        self.pc += 3

    def PRN(self, registry_index, param2):
        print(self.reg[registry_index])
        self.pc += 2

    def HLT(self, registry_index, param2):
        self.running = False
        self.pc += 1

    def MUL(self, registry_index_1, registry_index_2):
        mult = self.reg[0] * self.reg[1]
        self.reg[0] = mult
        print('mult', mult)
        # self.reg[0] = mult  How do i store this value?????
        self.pc += 3
    
    def PUSH(self, register_index, param2):
        #decrement stack pointer
        self.stack_pointer -= 1
        print(self.stack_pointer)
        #copy value at register_index 
        value = self.reg[register_index]
        # and put it in stack
        self.ram[self.stack_pointer] = value

        self.pc += 2

#possibly something wrong with stack_pointer in init

    def POP(self, register_index, param2):
        #copy value that stack pointer is pointing to
        value = self.ram[self.stack_pointer] 
        #place value at given register index
        self.reg[register_index] = value 
        #increment stack pointer
        self.stack_pointer += 1
        print(self.stack_pointer)
        #move program counter
        self.pc += 2




    def run(self):
        """Run the CPU."""
        

        while self.running:
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            #first instruction reads ram at 
            IR = self.ram_read(self.pc)
            self.branchtable[IR](operand_a, operand_b)













        

       
