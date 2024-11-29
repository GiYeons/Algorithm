# 미로 탐색 (풀이시간: 약 33분, 성공)
## 내 풀이
import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split())
graph = [[] for _ in range(n)]
distance = [[0] * m for _ in range(n)]

for i in range(n):
  str = read().strip()
  for s in str:
    graph[i].append(int(s))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 출발점
queue = deque([(0,0)])
distance[0][0] = 1

while queue:
  x, y = queue.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= n or nx < 0 or ny >= m or ny < 0:
      continue
    
    if graph[nx][ny] == 1 and distance[nx][ny] == 0:
      distance[nx][ny] = distance[x][y] + 1
      queue.append((nx, ny))

print(distance[n-1][m-1])

"""
한번 풀어봐서 풀이법이 기억이 났다.
큐에 append하는 것 잊지 말기.
그래프를 n+1, m+1로 만들고 싶었는데 귀찮아질것 같아서 그냥 했다
"""

## 정답
graph = [list(map(int, read().strip())) for _ in range(n)]
"""
문자열->리스트 변환은 위 한줄로 해결 가능
"""