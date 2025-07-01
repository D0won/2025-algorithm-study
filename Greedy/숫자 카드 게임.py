import sys

N,M = map(int, sys.stdin.readline().split())
matrix = []
for r in range(N) :
    matrix.append(list(map(int, sys.stdin.readline().split())))

minRow = 0
for r in range(N) :
    if min(matrix[r]) > minRow :
        minRow = min(matrix[r])

print(minRow)

""" 3-3.py min()함수를 이용하는 답안 예시
n, m = map(int, sys.stdin.readline().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n) :
    data = list(map(int, sys.stdin.readline().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""

"""3.4py 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, sys.stdin.readline().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data :
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""