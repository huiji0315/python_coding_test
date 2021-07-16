from collections import deque

def bfs(graph, start, visited):
    # bfs 구현 위해 사용하는 deque 라이브러리
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 방문 처리
        v = queue.popleft()
        print(v, end='')
        # 아직 방문하지 않은 경우 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# bfs 함수 호출(노드 1부터 시작)
bfs(graph, 1, visited)
