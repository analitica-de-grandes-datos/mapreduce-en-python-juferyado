#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

count = {}

for line in sys.stdin:
    if line in count:
        count[line] = count[line] + 1
    else:
        count[line] = 1

for item in count.items():
    print(item[0].rstrip() + '\t' + str(item[1]))
