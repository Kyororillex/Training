import sys

def main(lines):

    ans = 1

    for i in range(len(lines)): # 文字列の文字全てが異なる場合

        ans = ans * 2
    
    print(ans-1)  #空文字は除く

if __name__ == '__main__':

    lines = input()

    main(lines)
