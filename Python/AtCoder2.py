N, K, X = map(int, input().split())  # 3個の数字の入力を受け取る

str_list = list(map(int, input().split()))

str_list.sort(reverse=True)

for index, i in enumerate(str_list):

    while(i - X > 0):

        if K == 0:
            break

        else:
            i = i - X
            K -= 1
            str_list[index] = i

str_list.sort(reverse=True)

for index, i in enumerate(str_list):

    i = 0
    str_list[index] = i
    K -= 1

    if K == 0 or sum(str_list) == 0:
        break

print(sum(str_list))
