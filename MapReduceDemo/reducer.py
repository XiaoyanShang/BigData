import sys

last = ''
count = 0
for line in sys.stdin:
    word = line.split('\t')[0]
    if last == '':
        last = word
        count += 1
    elif word != last:
        print last + '\t' + str(count)
        last = word
        count = 1
    else:
        count += 1
print last + '\t' + str(count)       
