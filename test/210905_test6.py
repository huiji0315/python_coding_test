import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 하노이 원판 개수
n = int(input())

def hanoi(n, a, b, tmp):
    if n == 1:
        print(a, b)
    else:
        hanoi(n-1, a, tmp, b)
        print(a, b)
        hanoi(n-1, tmp, b, a)

print(2**n-1) # 원판이 n개 있다면 이동 횟수는 항상 2**n-1 이다.
if n <= 20: #  N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.
    hanoi(n, 1, 3, 2) # 3개의 장대

'''
# 하노이탑
https://www.acmicpc.net/problem/1914

[메모리 초과]
import sys
input = sys.stdin.readline

# 하노이 원판 개수
n = int(input())
# 원판 이동 횟수
cnt = 0
# 원판 이동 기록
move = []

def hanoi(n, a, b, tmp):
    global cnt
    if n == 1:
        move.append((a, b))
        cnt += 1
        return
    hanoi(n-1, a, tmp, b)
    move.append((a, b))
    cnt += 1
    hanoi(n-1, tmp, b, a)

hanoi(n, 1, 3, 2) # 3개의 장대
print(cnt)
for a, b in move:
    print(a, b)

-> 원판의 개수 N (1 ≤ N ≤ 100)
-> 원판 이동 기록을 모두 리스트에 저장을 하니까 메모리 초과가 발생했다.
리스트에 저장하지 않고 바로바로 출력해도 이동 순서대로 출력된다.
-> 또한, cnt 변수로 따로 구할 필요 없이 하노이탑에서는 원판이 n개 있다면 이동 횟수가 항상 2**n-1 이라고 한다.
'''
