import sys


N, M, K = map(int,sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
# 입력받은 수 내림차순 정렬
lst.sort(reverse= True)
# n은 더하는 횟수 확인
n = 0
# 큰 수 저장
bn = 0
# M만큼 반복
for _ in range(M) :
    # n 이 K번째 일 때 두번째로 큰 수를 더하고 n을 0으로 초기화
    if n == K :
        bn += lst[1]
        n = 0
    # n이 K번째가 아닐 때 가장 큰 수 더함.
    else :
        bn += lst[0]
    n += 1
print(bn)
""" 3 - 2.py 답안 예시

n, m, k = map(int, sys.stdin.readline().split()) 
data = list(map(int, sys.stdin.readline().split())

# 정렬
data.sort()
# 첫번째로 큰 수 저장
first = data[n-1]

# 두번째로 큰 수 저장
second = data[n-2]

# m을 k+1(첫 수 갯수 + 두번 째 수) 나눠 일정한 규칙의 묶음들을 계산, 묶음들 안에 있는 첫수의 개수를 곱함. 
count = int(m / k + 1) * k
# 블럭으로 못나눈 나머지 것들.. <- 이것도 첫 수임. 왜냐면 두번째 수가 나왔으면 묶음 처리될테니까.
count += m % (k + 1)

# 결과값 받을 변수
result = 0
result += count * first # -> 첫번째 수 count 만큼 곱함
result += (m - count) * second # -> m에서 첫번째 수 count를 뺀 나머지 값을 두번째 수에 곱함.

print(result)
"""