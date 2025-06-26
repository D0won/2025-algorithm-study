import sys

n = int(sys.stdin.readline())
money = [500, 100, 50, 10]
count = 0
for m in money :
    count += n // m
    n %= m

print(count)
