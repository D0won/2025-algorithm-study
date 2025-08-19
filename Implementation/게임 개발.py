import sys

# 맵의 세로 크기, 가로 크기를 입력받기
N, M = map(int, sys.stdin.readline().split())
# 게임 캐릭터가 있는 칸의 좌표와 바라보는 방향 d를 입력받기
A, B, d = map(int, sys.stdin.readline().split())

# 바라보는 방향으로 한칸 이동시키기 위한 변수 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 맵 생성
maps = []
# 맵 입력받기
for i in range(N) :
    maps.append(list(map(int, sys.stdin.readline().split())))

# 캐릭터가 현재 위치한 칸을 1로 번경
maps[A][B] = 1
# 캐릭터가 방문한 칸의 수를 받는 변수(현재 있는 칸까지 계산)
count = 1

while True :
    # 4방향 모두 접근불가인지 아닌지 여부 확인용 변수
    check = 0
    # 4방향 모두 갈 수 있는지 체크
    for _ in range(4) :
        # 캐릭터가 바라보고 있는 방향 기준으로 왼쪽이기에 -1을 해줌
        d = d - 1
        # 만약 -1이면 3으로 번경(dx, dy 리스트가 0~3이기 때문)
        if d == -1 :
            d = 3
        # 만약 캐릭터가 갈려고 하는 곳이 0이라면 1로 번경 후 캐릭터 위치 이동
        # 접근 가능(check = 1)으로 번경 그리고 방문한 칸의 수(count)를 1 증가
        if maps[A + dx[d]][B + dy[d]] == 0 :
            maps[A + dx[d]][B + dy[d]] = 2
            A  += dx[d]
            B  += dy[d]
            check = 1
            count += 1
            break
    # 4방향 모두 갈 수 없다면 현재 캐릭터가 바라보고 있는 방향에서 뒤로 가기
    if check == 0 :
        if maps[A - dx[d]][B - dx[d]] != 1 :
            A = A - dx[d]
            B = B - dy[d]
        # 만약 뒤가 바다라면 반복문 빠져나오기
        else :
            break
print(count)
        
'''
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
'''

