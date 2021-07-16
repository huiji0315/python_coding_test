def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end='')
    # 아직 방문하지 않은 경우 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드에 인접하게 연결되어 있는 노드들을 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문된 노드를 체크하기 위한 리스트
visited = [False] * 9

# dfs 함수 호출(노드 1부터 시작)
dfs(graph, 1, visited)
