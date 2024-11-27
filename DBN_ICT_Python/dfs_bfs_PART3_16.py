# 연구소 (풀이시간: 약 1시간, 실패)
## 내 풀이
import sys
import copy
read = sys.stdin.readline

N, M = map(int, read().split())
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
  l = [0]
  graph[i] = l + list(map(int, read().split()))

graph_sm = copy.deepcopy(graph)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, graph):
  graph[x][y] = 2
  for i in range(4):
    if 1 <= x + dx[i] and x + dx[i] <= M and 1 <= y + dy[i] and y + dy[i] <= N and graph[x + dx[i]][y + dy[i]] == 0:
      dfs(x + dx[i], y + dy[i], graph)


check = (1, 1)
result = 0

while True:
  # 세워진 벽 체크용
  case = 0

  for i in range(check[0], N + 1):
    for j in range(check[1], M + 1):
      if graph_sm[i][j] == 0:
        graph_sm[i][j] == 1
        check = (i, j)
        case += 1
      if case == 3:
        break
    if case == 3:
      break

  if case < 3:
    break
  else:
    case = 0

  for i in range(1, N + 1):
    for j in range(1, M + 1):
      if graph_sm[i][j] == 2:
        dfs(i, j, graph_sm)

  result = max(result, graph_sm.count(0))
  graph_sm = []
  graph_sm = copy.deepcopy(graph)
  

print(result)

"""
일단 지도가 최대여봤자 8x8로 굉장히 작음
그럼 완전탐색으로 풀어야하는걸까
모든 경우의수를?따진다면

처음부터 마지막까지 모든 경우의 수로 벽을 세워보고
바이러스를 퍼뜨린다
그러고나서 0의 개수를 세고
일단 말이안되지만 해볼까

시뮬용 맵 복사해두기

2중 for문으로 벽을 세워봄.. 하나 했으면 거기부터 또 하면 되잖아
for i rnag N
	for j M:
		i j = 1

for i in 위의 값부터 N까지

3번 반복... 벽의 위치 list에 저장해둘 것

def dfs(start, map):
	dfs는..일단 start에 2 처리하고
	start의 상하좌우 좌표를 확인하고
	2가 아니라면 하나하나 다시 dfs 하면 될거같다

이걸 매번 돌리며 0의 개수 업데이트. 기존의 result보다 좋으면 그걸로 업뎃하면 됨
"""

## 정답
N, M = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * M for _ in range(N)]  # 벽을 설치한 뒤의 맵 리스트

for _ in range(N):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색을 이용해 각 바이러스가 사방으로 퍼지게 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 상하좌우로 바이러스가 퍼질 수 있는 경우
    if 0 <= nx and nx < N and 0 <= ny and ny < M:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고 다시 재귀적 수행
        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score = 0
  for i in range(N):
    for j in range(M):
      if temp[i][j] == 0:
        score += 1

  return score

# 깊이 우선 탐색을 이용해 울타리를 설치하면서 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(N):
      for j in range(M):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(N):
      for j in range(M):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전 영역의 최대값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(N):
    for j in range(M):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)
  
"""
가능한 모든 경우의 수를 계산한다는 내 풀이법 자체는 맞았다.
벽의 개수가 3개가 되는 모든 조합을 찾은 후에 그러한 조합에 대해서 안전 영역의 크기를 계산하면
되는 것이다. 안전 영역의 크기를 구하는 것은 DFS나 BFS를 통해 할 수 있다.
울타리를 dfs를 통해 설치하는 아이디어가 정말 인상적인 듯.
"""