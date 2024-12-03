# 토마토 (풀이시간: 약 48분, 실패)
## 내 풀이
import sys
from collections import deque
INF = 1e9
read = sys.stdin.readline

m, n = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(n)]
day = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

executed = False
min_day = INF

def bfs(i, j):
  queue = deque([(i, j)])
  graph[i][j] = 1
  end_day = 0
  global executed
  global min_day

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i] 
      
      if nx >= n or nx < 0 or ny >= m or ny < 0:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        queue.append((nx, ny))
        # 기록
        executed = True
        day[nx][ny] = day[x][y] + 1
        end_day = max(end_day, day[nx][ny])

  min_day = min(end_day, min_day)


for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      bfs(i, j)

all_one = True
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      all_one = False
      
if executed == False:
  print(0)
elif all_one == False:
  print(-1)
else:
  print(min_day)

"""
로직은 맞는데 경우의 수를 다 처리를 못했다..라고 생각했는데 로직을 잘못 짰음
익은 토마토가 있는 곳을 하나씩 bfs 돌려서 최소 일자가 나오는 곳을 찾으면 된다고 생각했는데
사실 하루가 지날 때마다 모든 익토가 동시다발적으로 전파를 시작한다...
한번에 시도했어야 했다
----아이디어----
하루마다 인접한 4방향의 토마토가 익는다는 거지 즉 bfs임

우선 입력을 받고
max_day = 0
excuted = False
전 노드를 돌리면서 익토를 찾아야함
bfs(x, y)

bfs
	큐 선언..뽑고
	while을 돌리는데 4방향을 다 돌릴거임
	다 돌리면서 0으로 만든다
	한번이라도 만들었으면 executed = True
	한 루프가 끝나면 day += 1
	max(day, max_day)

만약 끝났는데 그래프에 0이 있으면 -1

각 그래프별로 봣을때 최대 day가 최소 day인 경우를 찾아야 함
"""

## 정답

  
"""
처음에 익힌 토마토가 있는 모든 위치를 큐에 넣고 시작했으면 되는 거였다
다시 풀어보고 정답 작성할 것!
"""