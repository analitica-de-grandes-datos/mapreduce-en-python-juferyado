#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for line in sys.stdin:
    number, chars = line.split('\t')

    for char in chars:
        if char != ',':
            print(f'{char},{number}')