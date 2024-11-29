# 단지번호붙이기 (풀이시간: 약 23분, 성공)
## 내 풀이
import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
graph = [list(map(int, read().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 집 개수 반환
def bfs(a, b):
  queue = deque([(a, b)])
  visited[a][b] = 1
  count = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue

      if graph[nx][ny] == 1 and visited[nx][ny] == 0:
        visited[nx][ny] = True
        queue.append((nx, ny))
        count += 1

  return count


danji = 0
house = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == 0:
      house.append(bfs(i, j))
      danji += 1

house.sort()
print(danji)
for i in range(danji):
  print(house[i])

"""
양배추랑 거의 똑같은 문제
"""

## 정답
import sys
from collections import deque

read = sys.stdin.readline
n = int(read())
graph = [list(map(int, read().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 집 개수 반환
def bfs(a, b):
  queue = deque([(a, b)])
  graph[a][b] = 0
  count = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1

  return count


danji = 0
house = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append(bfs(i, j))
      danji += 1

house.sort()
print(danji)
for i in range(danji):
  print(house[i])
  
"""
visited를 빼도 풀 수 있는 문제
"""