# 게임 개발
## 내 풀이 (풀이시간: 50분)
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
state = list(map(int, input().split()))
map = [list(map(int, read().split())) for _ in range(N)]

forward = [0, 1, 2 ,3]
step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(step[state[2]][0])

while True:
  prev_state = state

  for i in range(4):
    # 방향 갱신
    if state[2] > 0:
      state[2] = state[2] - 1
    else:
      state[2] = 3

    # 위치 갱신
    next_step = (state[0] + step[state[2]][0], state[1] + step[state[2]][1])

    if map[next_step[0]][next_step[1]] == 0:
      map[state[0]][state[1]] = 2
      state[0], state[1] = next_step[0], next_step[1]

  
  if prev_state[0:2] == state[0:2]:
    next_step = (state[0] - step[state[2]][0], state[1] - step[state[2]][1])
    if map[next_step[0]][next_step[1]] == 1:
      break
    else:
      state[0], state[1] = next_step[0], next_step[1]

print(count(map, 2))

"""
무한루프에 빠졌다. 원인은 모르겠다. 일단 내가 생각한 알고리즘은 이랬다.
forward = [0, 1, 2 ,3]
step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while True:
	원래 state 저장

	for i in range 4:

	다음 방향 = state[2] - 1인데 이 결과가 -1이면 3으로
	다음 스텝 = 방향에 따라 다음 스탭 좌표를 입력
	if 다음 스텝이 육지이고 가보지 않았다면:
		이전 스텝에 visited 2 체크 후 state 갱신
	elif 바다거나 가봤다면:
		state 갱신을 방향만 한다
	
	if 현재  state와 원래 state에서 좌표값이 동일하다면:
		if 현재 방향에서 뒤쪽 칸이 바다라면 break
		else:
			한칸 뒤로
	
result = 2의 개수
"""

## 답안
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
x, y, direction = map(int, input().split())
visited = [[0] * M for _ in range(N)]

visited[x][y] = 1  # 현재 좌표 방문 처리

map = [list(map(int, read().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if visited[nx][ny] == 0 and map[nx][ny] == 0:
    visited[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
    
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if map[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)

