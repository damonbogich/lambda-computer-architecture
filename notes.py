memory = [
    1, #print damon
    3, #Save register R2 99 --- register to save in (R2), value to save there (99)
    2, #              R2
    99,#                 99
    2, #Halt
    
]

register = [0] * 8

program_counter = 0 #program counter is index into memory of the current instruction
                    #Aka pointer to the current instruction
running = True

while running:
    instruction = memory[program_counter]

    if instruction == 1:
        print('Damon')
        program_counter += 1
    elif instruction == 2:
        running = False
    elif instruction == 3:
        register_number = memory[program_counter + 1]
        value = memory[program_counter + 2]

        register[register_number] = value
        
        program_counter += 3
        print(register)
    else:
        print(f"unknown instruction {instruction}")

# for instruction in memory:
#     if instruction == 1:
#         print('damon')
#     elif instruction == 2:
#         break
#     else:
#         print(f"unknowm instruction {instruction}")