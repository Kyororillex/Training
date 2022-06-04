N, K, X = map(int, input().split())  # 3個の数字の入力を受け取る

str_list = list(map(int, input().split()))

for index , i in enumerate(str_list):

    use_qoupon = int(i / X)

    if K - use_qoupon >= 0:
        str_list[index] = i - (use_qoupon * X)
        K = K - use_qoupon
    
    else:
        str_list[index] = i - (K * X)
        K = 0
        break
        
if K == 0:
    print(sum(str_list))
    
else:
    str_list.sort(reverse=True)

    if K >= len(str_list):
        print('0')

    else:
        for i in range(K):
            str_list[i] = 0

        print(sum(str_list))
