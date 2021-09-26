from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1 # 현재노드 방문처리
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[node] + 1 # 노드와 떨어진 거리

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)] # 각 노드와 연결된 노드
    visited = [0] * (n+1)
    for a, b in edge: # 양방향 연결
        graph[a].append(b)
        graph[b].append(a)

    bfs(graph, 1, visited)

    answer = visited.count(max(visited))
    return answer

'''
# [그래프(bfs)] 가장먼노드
https://programmers.co.kr/learn/courses/30/lessons/49189
'''
