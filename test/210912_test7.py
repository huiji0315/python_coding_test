import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, w):
    for e in graph[x]:
        node, wei = e
        if dist[node] == -1: # 업데이트 되지 않은 경우(방문하지 않은 경우)
            dist[node] = w + wei # 루트 노드에서의 거리 업데이트
            dfs(node, w + wei)

# 노드의 개수(1<=n<=10000)
n = int(input())
# 트리(tree)는 사이클이 없는 무방향 그래프
graph = [[] for _ in range(n+1)]

for i in range(1, n): # 간선 정보 입력
    # 부모 노드, 자식 노드, 간선의 가중치
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

# 루트 노드에서의 거리
dist = [-1] * (n+1)
# 루트 노드 번호 = 항상 1
dist[1] = 0
# 루트에서 가장 먼 노드 탐색(dist 업데이트)
dfs(1, 0)

# 위에서 찾은 루트에서 가장 먼 노드
s = dist.index(max(dist))
dist = [-1] * (n+1) # 초기화
dist[s] = 0 # 시작점을 해당 노드로 변경
dfs(s, 0) # 루트에서 가장 먼 노드에서 가장 먼 노드 탐색(dist 재업데이트)

print(max(dist))

'''
# 트리의 지름
https://www.acmicpc.net/problem/1967
= 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우의 두 노드 사이의 경로의 길이
= 가장 끝 노드끼리 거리 중, 가장 큰 가중치(거리)를 가지는 것

- 부모 노드의 번호가 작은 것이 먼저 입력되고
- 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다.
= 부모, 자식 노드 순으로 자동 정렬됨

참고) https://kyun2da.github.io/2021/05/04/tree's_diameter/
-> dfs를 두번 돌려 해결하는 문제여서 신기했다.
'''
