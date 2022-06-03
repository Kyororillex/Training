import sys

def file_open(file):
    data = []
    try:
        f = open(file, 'r', encoding='utf-8')
    except Exception:
        print("open error. not found file:", str(file))
        sys.exit(1)
    for line in f:
        line = line.strip() 
        line = line.replace('\n','') 
        line = line.split(" ") 
        data.append(line)
    f.close()
    return data

files = sys.argv

with open(files[2], "r") as tf:
    lines = tf.read().split(' ')

card = file_open(files[1])
count = 0


for i in lines:
    count += 1
    for x in range(3):
        for y in range(3):
            if card[x][y] == i:
                card[x][y] = 0
                if int(card[0][0]) + int(card[0][1])+int(card[0][2]) == 0 or int(card[1][0])+int(card[1][1])+int(card[1][2]) == 0 or  int(card[2][0])+int(card[2][1])+int(card[2][2]) == 0 or int(card[0][0])+int(card[1][0])+int(card[2][0]) == 0 or int(card[0][1])+int(card[1][1])+int(card[2][1]) == 0 or int(card[0][2])+int(card[1][2])+int(card[2][2]) == 0 :
                    print(count)
                    break
        else:
            continue
        break
    else:
        continue
    break


