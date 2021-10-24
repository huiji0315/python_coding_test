import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(x, y):
    # 상하좌우
    dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in dir:
        x2 = x + dx
        y2 = y + dy
        if 0 <= x2 < n and 0 <= y2 < m:
            if field[x2][y2] == 1 and not visited[x2][y2]:
                visited[x2][y2] = 1
                dfs(x2, y2)

tc = int(input())
for _ in range(tc):
    # 배추밭의 가로길이 m, 세로길이 n, 배추가 심어져있는 위치 개수 k
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        # 배추의 위치
        x, y = map(int, input().split())
        field[y][x] = 1

    # 배추흰지렁이 마리수
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j)
                cnt += 1

    print(cnt)
'''
# 유기농 배추
https://www.acmicpc.net/problem/1012
- 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면
총 몇 마리의 지렁이가 필요한지 알 수 있다.
-> 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.


[느낀점 정리]
1. 런타임에러 발생 -> 재귀쓸 때 sys.setrecursionlimit(int(1e6)) 까먹지 말기
2. 좌표 구현할 때, 배열은 행과 열의 순서로 구성되어있기 때문에
문제에서 (행, 열)로 주어질 때도 있고, (열, 행)으로 주어질때가 있으므로
주의해서 보고 구현해야 한다.
-> ex) field[y][x] = 1
3. not visited 만 체크할 것이 아니라 배추가 있는 곳에서 dfs를 돌려야 하므로
해당 조건도 빼먹지 말고 체크해주어야 한다.
4. 좌표가 벗어나는 경우도 있으므로 그러한 경우를 체크하는 부분도 빼먹지 말아야 한다.

# 저번에 풀때는 풀이를 보고 풀었는데, 이번에는 혼자 힘으로 풀 수 있었다.
'''
