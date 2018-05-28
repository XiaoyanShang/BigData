import sys

for line in sys.stdin:
    words = line.strip('\n').split(' ')
    for word in words:
        print word + '\t1'

