#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = []

for line in sys.stdin:
    if line != '\n':
    # Combine
        char, date, number = line.split('   ')
        mapped_tuple = (char, date, number.rstrip())
        temp.append(mapped_tuple)

# Reduce
temp = sorted(temp, key=lambda x: (x[0], int(x[2])))

# Format
for item in temp:
    print(f'{str(item[0])}   {item[1]}   {item[2]}')