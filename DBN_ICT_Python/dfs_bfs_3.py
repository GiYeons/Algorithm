# 음료수 얼려 먹기
## 내 풀이 (풀이시간: 40분, 실패)
import sys

N, M = map(int, input().split())
read = sys.stdin.readline
arr = []

for _ in range(N):
  arr.append(list(map(int, read().strip())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(graph, x, y):
  graph[x][y] = 1
  nxy_list = []
  
  for i in range(4):
    if x + dx[i] >= 0 and x + dx[i] < M and y + dy[i] >= 0 and y + dy[i] < N:
      if arr[x + dx[i]][y + dy[i]] == 0:
        nxy_list.append((x + dx[i], y + dy[i]))

  if nxy_list:
    for xy in nxy_list:
      dfs(xy[0], xy[1])


while arr.count(0) != 0:
  idx = -1
  
"""
구현 방법을 모르겠어서 중도 포기
--아이디어--
N, M 가로세로길이
얼음틀 입력.
뚫림 1 막힘 1

동서남북 방향 배열 만들어두기

배열을 돌면서 일단 0을 찾는다
0을 하나 찾으면 그걸로 dfs를 돌리면서 다 visited로 만든다
그걸 몇번 햇는지 카운트한다

while 맵 find 0이 -1일 때까지:
	맵 find 0해서 인덱스 저장
	그 x y로 dfs를 돌린다
	count+= 1


dfs(맵, x, y):
	일단 들어온 좌표를 방문처리
	xylist = 
	인덱스를 벗어나지 않는 선에서 사방을 탐색. 0 좌표 저장
	dfs(x, y)
"""

## 정답
import sys

N, M = map(int, input().split())
read = sys.stdin.readline
graph = []

for _ in range(N):
  graph.append(list(map(int, read().strip())))


def dfs(x, y):
  # 주어진 범위를 벗어나는 경우 즉시 종료
  if x <= -1 or x >= N or y <= -1 or y >= M:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상하좌우 위치 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False

result = 0
for i in range(N):
  for j in range(M):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)

"""
아이디어 자체는 내가 생각한 것과 같다.
1. 특정 지점의 상하좌우를 살펴보고, 주변 지점 중 값이 0이면서 아직 방문하지 않은 지점을 방문한다.
2. 방문한 지점에서 다시 상하좌우를 살펴보며 방문을 다시 진행한다.
3. 1~2를 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.

다만 코드가 내가 생각못해본 구조다...일단 나는 index나 find 함수를 이용해서 0의 위치를
찾으려고 했는데 그냥 이중 for문을 돌리면서 모든 노드를 방문하면 되는 거였다.
그리고 dfs가 0을 찾아 방문처리를 했다면 True, 칸막이였다면 False를 반환한다.
이를 통해 뚫려있는 공간의 개수를 셌다. 그리고 상하좌우에 대해 모두 dfs를 수행한다.
기존에 알던 DFS 그래프 구현 코드랑은 다르지만...내생각에 재귀가 있다면 일단 DFS를 의심해야지
싶다.
"""