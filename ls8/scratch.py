import sys

memory = [0] * 256

register = [0] * 8



# file_name = sys.argv[1]
with open('examples/print8.ls8') as f:
    address = 0

    for line in f:
        line = line.split('#')
        try:
            v = line[0].strip()
        except ValueError:
            continue
        if len(v) > 0:
            memory[address] = int(v,2)
            address += 1


print('memmory', memory[:15])
print(0b10000010 == 130)

sys.exit(0)

# 'examples/print8.ls8'

