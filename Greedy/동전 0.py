import sys

# 동전 종류 및 가치의 합 입력받기
N, K = map(int,sys.stdin.readline().split())
# 동전 종류별로 입력받을 리스트 저장
money = []
# 동전 종류별로 입력받기
for m in range(N) :
    money.append(int(sys.stdin.readline()))
# 동전 종류를 내림차순으로 정렬
money = sorted(money, reverse=True)
# 동전 갯수를 저장하는 변수
n = 0
# 내림차순으로 동전 크기를 낮추면서 갯수를 저장
for m in money :
    n += K // m
    K %= m

print(n)