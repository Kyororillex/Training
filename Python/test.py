import sys

query = sys.argv

if len(query) != 3:
    sys.exit(1)

n = int(query[1])

print(n)