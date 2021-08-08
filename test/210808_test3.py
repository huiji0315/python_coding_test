# 정점의 개수 N, 간선의 개수 M
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

# 간선의 양 끝점 u와 v
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i, visited)

# 연결요소 개수
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i, visited)

print(cnt)

'''
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하기

연결요소의 개수를 세기 위해서는 dfs로 돌면서 체크하면 된다.
1번 노드부터 dfs를 돌면서 방문되지 않은 노드들은 계속 dfs를 돌고,
시작한 노드로부터 dfs를 다 돌았을 경우에는 다시 2번 노드를 살펴봐서 방문되지 않았다면, 하나의 연결요소로 이루어져 있지 않다는 것을 의미한다.
따라서 연결요소의 개수를 하나 늘리고 dfs를 다시 돌리면 된다.
이런 식으로 전체 노드를 한 번씩 확인하여 연결요소의 개수를 구할 수 있다.

[문제점 정리]
1. n, m = map(int, input().split())에서
n, m = int(input().split())으로 작성하는 어이없는 실수를 했다.
-> TypeError: int() argument must be a string a bytes-like object or a number not 'nonetype'가 발생한다. list를 바로 int로 변환시켜줄 수 없다는 내용이다.

2. graph = [[] for _ in range(n+1)]에서 저번에 정리했던 list_comprehension 부분을 다시 찾아보았다.

3. 주어지는 정점의 값이 1~n이기 때문에 n+1 길이의 리스트를 활용해야하고,
정점을 방문할 때에도 1부터 방문하면 된다.

4. 그래프에서 정점이 주어진 것이 아니라 간선의 양 끝 정점이 주어져서
이것을 어떻게 정점으로 바꾸는지에 대해 빠르게 생각하지 못했다.
dfs의 경우 시작 정점부터 인접한 정점들을 방문하는 것이기 때문에
인접리스트를 이용해서 정점으로 변환시킬 수 있다.
예를 들어 1번 정점과 2번 정점이 어떤 간선의 양 끝점이라면
1번 정점의 인접 리스트 원소에 2번 정점이 들어가고,
반대로 2번 정점의 인접리스트 원소에도 1번 정점이 들어가도록 설정해주면 된다.
'''
