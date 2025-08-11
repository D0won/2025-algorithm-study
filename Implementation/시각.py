import sys

# N시 입력 받기
N = int(sys.stdin.readline())
# 3의 개수를 받는 변수
count = 0

for t in range(N + 1) :
    for m in range(60) :
        for s in range(60) :
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(t) + str(m) + str(s) :
                count += 1

print(count)