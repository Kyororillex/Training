# N , K= map(int, input().split())

# l = list(map(int, input().split()))

N , K = 3 , 5

l = [4,5,3]

if N < K :

    for index , i in enumerate(l) :
        
        print(i)

        l[index] = 0

print(l)