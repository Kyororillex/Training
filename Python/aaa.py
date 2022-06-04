n = map(int , input())
str_list = list(map(int, input().split()))

s = ''

str_list.sort()

print('%d %d' %(str_list[0],str_list[len(str_list)-1]) )

for i in str_list:
    print(i,end='')