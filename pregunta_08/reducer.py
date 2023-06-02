#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = {}

for line in sys.stdin:
    # Combine
    if line != '\n':
        key, value = line.split(',')
        value = value.rstrip()

        if key not in temp:
            temp[key] = [float(value)]
        else:
            temp[key].append(float(value))

# Reduce
for item in temp:
    temp[item] = [sum(temp[item]), sum(temp[item]) / len(temp[item])]

# Format
for item in temp.items():
    print(f'{str(item[0])}\t{item[1][0]}\t{item[1][1]}')