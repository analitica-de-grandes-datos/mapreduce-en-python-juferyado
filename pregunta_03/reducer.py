#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = {}

for line in sys.stdin:
    # Combine
    if line != '\n':
        key, value = line.split(',')
        temp[key] = value.rstrip()

# Reduce
temp = sorted(temp.items(), key=lambda x: x[1])

# Format
for item in temp:
    print(f'{item[0]},{item[1]}')
