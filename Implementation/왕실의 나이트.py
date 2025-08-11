import sys

# 위치 입력받기
loc = sys.stdin.readline()

# 열이 문자로 들어오므로 딕셔너리를 통해 숫자로 바꿈
dic = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
# 나이트의 모든 이동 경로
dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

# 나이트는 총 8가지의 움직임이 가능함.
count = 8
# 8가지의 움직임 중 안되는 경우를 따져 하나씩 지움
for i in range(8) :
    x = dic[loc[0]]
    y = int(loc[1])

    x += dx[i]
    y += dy[i]

    if x < 1 or x > 8 or y < 1 or y > 8 :
        count -= 1

print(count)

# # 예제 답안

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# # 입력된 문자의 ASCII 값을 'a'의 ASCII 값과 비교해 1부터 시작하는 열
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps :
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
#         result += 1

# print(result)