# 미로 탈출
## 내 풀이 (풀이시간: 13분)
"""
모르겠고 안 풀릴것 같아서 중도 포기.
"""

## 답
from collections import deque
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, read().strip())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 사방으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문한 경우에만 최단거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단거리 반환
  return graph[N-1][M-1]

print(bfs(0,0))

"""
아이디어가 낯설고 어려웠다. BFS를 이용하여 모든 노드의 값을 거리 정보로 넣을 수 있다고 한다.
특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.
이때 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록하므로 모든 노드는 (1,1) 지점으로부터의
최단 거리만을 기록한다.
BFS기 때문에 네 방향으로의 위치를 확인할 때마다 확인한 노드를 새로이 큐에 넣어야 한다.
"""