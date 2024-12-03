# 적록색약 (풀이시간: 약 40분, 성공)
## 내 풀이
import sys
sys.setrecursionlimit(10000)
read = sys.stdin.readline

n = int(read())
graph = [list(read().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if visited[x][y] == 1:
        return
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        if graph[x][y] == graph[nx][ny]:
            dfs(nx, ny)

result1 = 0
result2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result1 += 1

# 적록 구역개수
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result2 += 1

print(result1, result2)

"""
로직은 단순하다고 생각했다. 처음에는 맵이 주어진 대로 구역 개수를 세고... 두번째로는
G를 R로 바꿔서 다시 똑같이 개수를 셈
bfs로만 문제를 풀었더니 bfs가 낯설어서 난항을 겪었다
인덱스 아웃이 안되게 코드 추가하는걸 자꾸 잊음...
"""

## 정답

  
"""
내가 생각한 로직이 맞음
"""