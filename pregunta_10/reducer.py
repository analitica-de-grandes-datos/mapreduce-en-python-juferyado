#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temp = {}

for line in sys.stdin:
    # Combine
    if line != '\n':
        key, value = line.split(',')

        if key != '':
            value = value.rstrip()

            if key not in temp:
                temp[key] = [int(value)]
            else:
                temp[key].append(int(value))

# Reduce
for item in temp.items():
    print(f'{item[0]}\t{",".join(list(map(lambda x: str(x), sorted(item[1]))))}')