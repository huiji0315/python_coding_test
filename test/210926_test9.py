import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    visited[start] = 1
    dp[start][1] = people[start]
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            # 현재 마을을 우수마을로 선정하는 경우
            # 인접한 마을을 선정할 수 없다.
            dp[start][1] += dp[i][0]
            # 현재 마을을 우수마을로 선정하지않는 경우
            # 인접한 마을을 선정하거나 선정하지 않는 두 가지 경우를 모두 고려해야 한다.
            dp[start][0] += max(dp[i][0], dp[i][1])

# n개의 마을
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
# 마을 주민 수
people = [0] + list(map(int, input().split()))
# 마을 주민 수의 총합이 최대가 되는 경우를 구하기 위한 dp
# dp[n][1] = n번 마을을 우수마을로 선정했을 경우에 우수 마을의 주민 수의 총합
# dp[n][0] = n번 마을을 우수마을로 선정하지 않았을 경우에 우수 마을의 주민 수의 총합
dp = [[0, 0] for _ in range(n+1)]

# 마을과 마을 사이를 직접 잇는 n-1개의 길
for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(max(dp[1][1], dp[1][0]))

'''
# 우수마을
https://www.acmicpc.net/problem/1949

[우수마을의 조건]
1. '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
2. 마을 사이의 충돌을 방지하기 위해서, 만일 두 마을이 인접해 있으면 두 마을을 모두 '우수 마을'로 선정할 수는 없다. 즉 '우수 마을'끼리는 서로 인접해 있을 수 없다.
3. 선정되지 못한 마을에 경각심을 불러일으키기 위해서, '우수 마을'로 선정되지 못한 마을은 적어도 하나의 '우수 마을'과는 인접해 있어야 한다.

-> 우수 마을의 주민 수의 총 합 출력하기

DFS까지는 했는데, 마을들이 인접할 수 없도록 하면서 총합을 최대로 하는 방법에 대해서 생각하기 힘들었다.
-> DP를 활용한 DFS로 풀이하면 된다.

참고) https://ca.ramel.be/132
'''
