import sys

def main(lines):

    for i, v in enumerate(lines):

        a = int(v.split(' ')[0])

        b = int(v.split(' ')[1])

        n = int(v.split(' ')[2])
    
    index = 0
    point = a

    while point <= n:

        if index % 7 == 0 and index != 0:

            point = point + b
            index += 1

        else:

            point = point + a
            index += 1

    print(index-1)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
