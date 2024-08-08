# 뱀 (풀이시간: 약 55분, 실패)
## 내 풀이
import sys
from collections import deque
read = sys.stdin.readline

N = int(read())
K = int(read())
apple = [tuple(map(int, read().split())) for _ in range(K)]
L = int(read())
direct_conv = [tuple(read().split()) for _ in range(L)]

# 맵 생성
map = [[0] * N for _ in range(N)]
apple_map = [[0] * N for _ in range(N)]
for a in apple:
  i, j = a
  apple_map[i-1][j-1] = 1

# 우 하 좌 상
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# 변수 및 초기화
time = 0 
map[0][0] = 1
body = deque()
body.append((0, 0))
direct = 0

while True:
  x, y = body.pop()
  body.append((x, y))
  x += direction[direct][0]
  y += direction[direct][1]

  if x < 0 or x >= N or y < 0 or y >= N:
    break
  if map[x][y] == 1:
    break

  if apple_map[x][y] == 0:
    dx, dy = body.popleft()
    map[dx][dy] = 0
    
  body.append((x, y))
  map[x][y] = 1

  direct_info = direct_conv[0]
  if time == int(direct_info[0]):
    if direct_info[1] == "L":
      direct =- 1
    else:
      direct += 1
      
    if direct >= 4:
      direct = 0
    elif direct < 0:
      direct = 3
    del direct_conv[0]

  time += 1

print(time)

"""
로직 잘 짰다고 생각했는데 실패했다니 슬프다...
답지 보고 고칠 수 있으면 고쳐보자
"""

## 정답
import sys
read = sys.stdin.readline

n = int(read())
k = int(read())
data = [[0] * (n + 1) for _ in range(n + 1)]  # 맵 정보
info = []  # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, read().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(read())
for _ in range(l):
  x, c = read().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x, y = 1, 1  # 뱀의 머리 위치
  data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
  direction = 0  # 처음에는 동쪽을 보고 있음
  time = 0  # 시작한 뒤에 지난 '초' 시간
  index = 0  # 다음에 회전할 정보
  q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      # 사과가 없다면 이동 후에 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후에 꼬리 그대로 두기
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸에 부딪혔다면
    else:
      time += 1
      break
    x, y = nx, ny  # 다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())
    