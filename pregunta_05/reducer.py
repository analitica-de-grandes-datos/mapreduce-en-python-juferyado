#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = {}

for line in sys.stdin:
    # Combine
    line = line.rstrip()
    if line not in temp:
        temp[line] = [line]
    else:
        temp[line].append(line)

# Reduce
for item in temp:
    temp[item] = len(temp[item])

# Format
for item in temp.items():
    print(f'{item[0]}\t{str(item[1])}')