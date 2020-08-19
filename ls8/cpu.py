"""CPU functionality."""

import sys


LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010

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


    def run(self):
        """Run the CPU."""
        #set binary code to variables
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        MUL = 0b10100010

        running = True

        while running:
            #first instruction reads ram at 
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == HLT:
                running = False
                self.pc += 1
            elif IR == LDI:
                self.reg[0] = 8
                self.reg[1] = 9
                self.pc += 3
            elif IR == PRN:
                print(self.reg[0])
                self.pc += 2
            elif IR == MUL:
                mult = self.reg[0] * self.reg[1]
                print(mult)
                # self.reg[0] = mult  How do i store this value?????
                self.pc += 3


        #reads memory address and stores it in Instruction register
        
        #Some instructions requires up to the next two bytes of data _after_ the `PC` in
        # memory to perform operations on. Sometimes the byte value is a register number,
        # other times it's a constant value (in the case of `LDI`). Using `ram_read()`,
        # read the bytes at `PC+1` and `PC+2` from RAM into variables `operand_a` and
        # `operand_b` in case the instruction needs them.
        
#         Then, depending on the value of the opcode, perform the actions needed for the
        # instruction per the LS-8 spec. Maybe an `if-elif` cascade...? There are other
        # options, too.

        

       
