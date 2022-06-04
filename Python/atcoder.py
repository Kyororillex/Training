nyuuryoku = input().split()

N = int(nyuuryoku[0])

A = int(nyuuryoku[1])

B = int(nyuuryoku[2])

for i in range(N):

    for j in range(A):

        for l in range(N):

            if (l % 2 == 0 and i % 2 == 0 or l % 2 != 0 and i % 2 != 0) :
                for b in range(B):
                    print('.',end='')
        
            else:
                for b in range(B):
                    print('#',end='')

        print()
