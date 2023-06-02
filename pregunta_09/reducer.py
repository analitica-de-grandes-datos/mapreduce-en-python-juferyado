#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = []

for line in sys.stdin:
    # Combine
    if line != '\n':
        char, date, number = line.split('   ')
        mapped_tuple = (char, date, int(number))

        temp.append(mapped_tuple)

# Reduce
temp = sorted(temp, key=lambda x: x[2])[:6]

# Format
for item in temp:
    print(f'{str(item[0])}   {item[1]}   {item[2]}')