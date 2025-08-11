import sys

# 정사각형(map)의 한 변의 길이 입력 받기
n = int(sys.stdin.readline())
# 여행가가 이동할 계획서 내용 입력 받기
plan = sys.stdin.readline().split()
# 맨 처음 좌표 생성
x = 1
y = 1
# 여행가의 계획서에 따라 움직임 요구(이 때 맵 밖으로 벗어나지 않도록 제어)
for p in plan :
    if p == 'R' and y < n:
        y += 1
    elif p == 'L' and y > 1:
        y -= 1
    elif p == 'U' and x > 1:
        x -= 1
    elif p == 'D' and x < n:
        x += 1

print(x,y)

# # 예제 답안 예시

# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L,R,U,D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1,1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인
# for plan in plans :
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)) :
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n :
#         continue
#     # 이동 수행
#     x, y = nx, ny

# print(x, y)