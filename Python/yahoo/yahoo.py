import sys

def main(lines):
    
    for i, v in enumerate(lines):
        
        score = int(v.split(' ')[1])

        if i == 0:

            important = int(v.split(' ')[1])

        elif score >= important:

             print(v.split(' ')[0])
            
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)