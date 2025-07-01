# 예제 답안과 내 답안이 같으므로 예제 답안 제외

import sys

# 입력 받기
n = int(sys.stdin.readline())
# 화폐 종류(갯수 : K)
money = [500, 100, 50, 10]
# 화폐 갯수
count = 0
# 화폐 종류별로 나누어 count 변수에 저장
for m in money :
    count += n // m
    n %= m
# 출력
print(count)

# 예제 답안과 내 답안이 같으므로 예제 답안 생략
