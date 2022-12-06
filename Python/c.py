import copy

N, K= map(int, input().split())  # 3個の数字の入力を受け取る

changed = []

count = 0

str_list = list(map(int, input().split()))

list2 = copy.copy(str_list)

list2.sort()

if list2 == str_list:
    print('Yes')

else:
    changeableare = N - K

    for i in range(changeableare):

        if str_list[i] > str_list[i+K]:

            count += 1

            str_list[i] , str_list[i+K] = str_list[i+K] , str_list[i]

            changed.append(i)
    
    if count == 0:
        print('No')




