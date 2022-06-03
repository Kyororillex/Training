import sys

def file_open(file):
    data = []
    try:
        f = open(file, 'r', encoding='utf-8')
    except Exception:
        print("open error. not found file:", str(file))
        sys.exit(1)
    for line in f:
        line = line.strip() #前後空白削除
        line = line.replace('\n','') #末尾の\nの削除
        line = line.split(" ") #分割
        data.append(line)
    f.close()
    return data

with open("numbers.txt", "r") as tf:
    lines = tf.read().split(' ')
    
card = file_open('card.txt')

print(card)
print(lines)