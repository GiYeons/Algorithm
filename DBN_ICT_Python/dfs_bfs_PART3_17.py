# 경쟁적 전염 (풀이시간: 약 13분, 포기)
## 내 풀이
"""
풀이가 생각이 안 난다...
"""

## 정답 
from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())

graph = []  # 전체 보드 정보
data = []  # 바이러스 정보

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, read().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # 바이러스 종류, 시간, 위치 X, 위치 Y 삽입
      data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, read().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:
  virus, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])

"""
이 문제는 BFS로 해결할 수 있다. 낮은 번호부터 증식하므로 큐에는 낮은 번호의 바이러스부터
삽입한다.
"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2