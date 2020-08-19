import sys

memory = [0] * 256

address = 0



if len(sys.argv) != 2:
    print('usage, comp.py filename')
    sys.exit(1)

try: 
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                line = line.split('#', 1)[0]
                line = int(line, 10)
                memory[address] = line
                address += 1
            except ValueError:
                pass
except FileNotFoundError:
    print(f"couldn't find file {sys.argv[1]}")
    sys.exit(1)


register = [0] * 8



program_counter = 0 #program counter is index into memory of the current instruction
                    #Aka pointer to the current instruction

fl = 0

SP = 7

register[SP] = 0xf4 #seets register 7 as stack pointer

running = True

while running:
    IR = memory[program_counter]

    if IR == 1:
        print('Damon')
        program_counter += 1
    elif IR == 2: #HLT
        running = False
    elif IR == 3: #save register
        register_number = memory[program_counter + 1]
        value = memory[program_counter + 2]

        register[register_number] = value
        
        program_counter += 3
        print(register)
    elif IR == 4: #print register
        register_number = memory[program_counter + 1]
        print(register[register_number])

        program_counter += 2
    elif IR == 5: #push
        #decrement stack pointer
        #just decrementing the index in RAM that r[7] is pointing to
        register[SP] -= 1

        #get register value
        register_number = memory[program_counter + 1]
        value = register[register_number]

        address_to_push_to = register[SP]
        memory[address_to_push_to] = value

        program_counter += 2
    
    elif IR == 6:#POP
        address_to_pop_from = register[SP]
        value = memory[address_to_pop_from]

        register_number = memory[program_counter + 1]
        register[register_number] = value

        register[SP] =+ 1

        #incrment stack pointer
        program_counter += 2



    else:
        print(f"unknown instruction {IR}")






