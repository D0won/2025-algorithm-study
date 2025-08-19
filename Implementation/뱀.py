import sys
from collections import deque

# 보드의 크기 받기
N = int(sys.stdin.readline())

# 사과의 개수 받기
K = int(sys.stdin.readline())

# 보드판 설정
board = [[0] * N for _ in range(N)]

# 사과 위치 설정
for _ in range(K) :
    row, columns = map(int, sys.stdin.readline().split())
    board[row - 1][columns - 1] = 2

# 뱀의 방향 변환 정보 받기
L = int(sys.stdin.readline())

# 뱀의 방향 변환 정보 저장
directions = deque()
for _ in range(L) :
    X, C = sys.stdin.readline().split()
    directions.append((int(X), C))

# 초기 위치
x = 0
y = 0

# 초기 위치 1로 두기
board[x][y] = 1

# 뱀 위치 저장
body = deque()
body.append([x, y])

# 동,서,남,북 방향 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 방향 설정
d = 0

# 시간 저장 변수
time = 0

# 시뮬레이션 시작
while True :
    # 시간 추가
    time += 1

    # 뱀 이동
    x += dx[d]
    y += dy[d]

    # 뱀 이동위치 저장
    body.append([x, y])
    
    # 만약에 몸에 닿았거나 벽에 닿았을 때 시뮬레이션 중지
    if x < 0 or x >= N or y < 0 or y >= N or board[x][y] == 1:
        break
    
    # 사과를 먹었을 때는 1로 설정해두기
    if board[x][y] == 2 :
        board[x][y] = 1
    # 사과를 먹지 못했을 경우 꼬리 위치를 0으로 설정
    else :
        board[x][y] = 1
        bodyp = body.popleft()
        board[bodyp[0]][bodyp[1]] = 0
    
    # 만약에 방향 정보가 있고 시간이 다 되면 방향 옮기기
    if directions and directions[0][0] == time :
        xx, cc = directions.popleft()
        if cc == 'D' :
            d = d + 1
        else :
            d = d - 1

        if d == -1 :
            d = 3
        if d == 4 :
            d = 0
print(time)