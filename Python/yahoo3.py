import sys

a = 100
b = 1
n = 1000

index = 0
point = a
texindex = '0'

while point <= n:

    if '7' in texindex:

        point = point + b
        index += 1
        texindex = str(index)

    else:

        point = point + a
        index += 1
        texindex = str(index)

print(index)
