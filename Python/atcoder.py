import sys

def main(lines):

    for v in lines:

        a = str(v.split(' ')[0])

    print(a[-2:])

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
