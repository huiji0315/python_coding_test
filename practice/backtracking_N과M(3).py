n, m = map(int, input().split())
result = []

def dfs(count):
    if count == m:
        print(*result)
        return
    for i in range(1,n+1):
        result.append(i)
        dfs(count+1)
        result.pop()

dfs(0)

'''
# [백트래킹] N과M(3)
https://www.acmicpc.net/problem/15651
-> 중복 순열을 구하는 문제다.

참고) https://paris-in-the-rain.tistory.com/73


* 라이브러리를 사용해서 풀이하는 경우
https://juhee-maeng.tistory.com/91

1) 순열 (permutations(반복 가능한 객체, 뽑는 개수 r))
from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")
# (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)

2) 조합 (combinations(반복 가능한 객체, 뽑는 개수 r))
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")
# (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)

3) 중복순열 (product(반복 가능한 객체, repeat=1))
from itertools import product

for i in product([1,2,3],'ab'):
    print(i, end=" ")
# (1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b')

for i in product(range(3), range(3), range(3)):
    print(i, end=" ")
# (0, 0, 0) (0, 0, 1) (0, 0, 2) (0, 1, 0) (0, 1, 1) (0, 1, 2) (0, 2, 0) (0, 2, 1) (0, 2, 2) (1, 0, 0) (1, 0, 1) (1, 0, 2) (1, 1, 0) (1, 1, 1) (1, 1, 2) (1, 2, 0) (1, 2, 1) (1, 2, 2) (2, 0, 0) (2, 0, 1) (2, 0, 2) (2, 1, 0) (2, 1, 1) (2, 1, 2) (2, 2, 0) (2, 2, 1) (2, 2, 2)

for i in product([1,2,3], repeat=2):
    print(i, end=" ")
# (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)

for i in product([1,2,3], repeat=3):
    print(i, end=" ")
# (1, 1, 1) (1, 1, 2) (1, 1, 3) (1, 2, 1) (1, 2, 2) (1, 2, 3) (1, 3, 1) (1, 3, 2) (1, 3, 3) (2, 1, 1) (2, 1, 2) (2, 1, 3) (2, 2, 1) (2, 2, 2) (2, 2, 3) (2, 3, 1) (2, 3, 2) (2, 3, 3) (3, 1, 1) (3, 1, 2) (3, 1, 3) (3, 2, 1) (3, 2, 2) (3, 2, 3) (3, 3, 1) (3, 3, 2) (3, 3, 3)

'''
