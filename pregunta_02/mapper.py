#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    print(f"{line.split(',')[3]},{line.split(',')[4]}")