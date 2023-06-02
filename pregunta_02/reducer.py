#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


temp = {}

for line in sys.stdin:
    # Combine
    purpose, amount = line.split(',')

    if purpose not in temp:
        temp[purpose] = [int(amount)]
    else:
        temp[purpose].append(int(amount))

# Reduce
for item in temp:
    temp[item] = max(temp[item])

# Format
for item in temp.items():
    print(item[0].rstrip() + '\t' + str(item[1]))
