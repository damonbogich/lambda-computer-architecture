"""
CPU STACK
---------

Built into CPU

push/pop

Stack grows down 


WHAT DO YOU NEED FOR A STACK TO EXIST?
1. Store items in RAM
2. Stack pointer to the top of the stack (most recently pushed stack item)


Register 7 is reserved as the stack pointer
    *will contain the address in memory (RAM) of most recently pushed item to stack
    *if stack is empty, stack pointer points to F4 in RAM -- most recent key pressed on keyboard
    *It's there, because that's one index higher than the start of the stack
    * Stack is empty if stack pointer is F4


PUSH:
1. Decrement Stack pointer
2. copy value from register into memory at stack pointer's address


POP:
1. Copy value from address pointed to by stack pointer, to the given register
2. Imcrements Stack pointer
3. Just leave the value in RAM.  Value will be overwritten next time something is pushed to that address in RAM.
4. If you pop on an empty stack it will just move to the next RAM address


"""