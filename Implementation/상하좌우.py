import sys

n = int(sys.stdin.readline())
plan = sys.stdin.readline().split()
x = 1
y = 1

for p in plan :
    if p == 'R' :
        x += 1
    elif p == 'L' :
        x -= 1
    elif p == 'U' :
        y += 1
    else :
        y += -1

print(x, y)