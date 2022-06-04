import requests
import json
import sys

ans_list = []

def askSever(n,seed):

    url = "http://challenge-server.code-check.io/api/recursive/ask"

    url = url + '?n=' + str(n) + '&seed=' + seed

    data = requests.get(url)

    text = data.text

    data = json.loads(text)

    ans = data["result"]
    
    return ans

def f(n,seed):

    if n == 0:
        return 1

    elif n == 2:
        return 2

    elif n % 2 == 0:
        ans = f(n-1,seed) + f(n-2,seed) + f(n-3,seed) + f(n-4,seed)
        return ans
        
    else:
        ans = askSever(n,seed)
        return ans

query = sys.argv

if len(query) != 3:
    sys.stdout.write("エラー")
    sys.exit(1)

seed = query[1]

try:
    n = int(query[2])

except:
    sys.stdout.write("エラー")
    sys.exit(1)

ans = f(n,seed)

print(ans)
