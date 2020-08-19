import sys

memory = [0] * 256

register = [0] * 8

file_name = sys.argv[1]
with open(file_name) as f:
    address = 0

    for address, line in enumerate(f):
        line = line.split('#')
        try:
            v = int(line[0])
        except ValueError:
            continue
        memory[address] = v


print('memmory', memory[:15])

sys.exit(0)



program_counter = 0 #program counter is index into memory of the current instruction
                    #Aka pointer to the current instruction
running = True

while running:
    IR = memory[program_counter]

    if IR == 1:
        print('Damon')
        program_counter += 1
    elif IR == 3:
        running = False
    elif IR == 4:
        register_number = memory[program_counter + 1]
        value = memory[program_counter + 2]

        register[register_number] = value
        
        program_counter += 3
        print(register)
    else:
        print(f"unknown instruction {IR}")






