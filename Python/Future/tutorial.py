import sys

#10進数で表されたnけたの整数を並び替えた時にできる最小の整数を出力する

def main(str_num):

    zero_quantity = str_num.count('0')

    zero = ''

    for i in range(zero_quantity):

        zero = zero + '0'

    sorted_str_num = "".join(sorted(str_num))

    min_num = int(sorted_str_num)

    sorted_str_num = str(min_num)

    print(sorted_str_num[0] + zero + sorted_str_num[1:])

if __name__ == '__main__':
    
    # lines = []
    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))

    print('整数を入力:',end='')

    lines = input()

    main(lines)
