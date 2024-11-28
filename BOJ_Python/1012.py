# 유기농 배추 (풀이시간: 약 40분, 성공)
## 내 풀이
import sys
sys.setrecursionlimit(100000)

read = sys.stdin.readline
T = int(read())

# dfs
def dfs(x, y):
  if graph[x][y] == 0:
    return

  graph[x][y] = 0

  for i in range(4):
    if x + 1 < N:
      dfs(x + 1, y)
    if x - 1 >= 0:
      dfs(x - 1, y)
    if y + 1 < M:
      dfs(x, y + 1)
    if y - 1 >= 0:
      dfs(x, y - 1)

result = []
for _ in range(T):
  M, N, K = map(int, read().split())
  graph = [[0] * M for _ in range(N)]

  for i in range(K):
    X, Y = map(int, read().split())
    graph[Y][X] = 1

  count = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        dfs(i, j)
        count += 1

  result.append(count)

for r in result:
  print(r)

"""
재귀 횟수 제한에 걸려서 제한을 풀었다. DFS 대신 BFS를 쓰는게 나았나 싶다.
테스트 케이스까지 내가 신경써야 하는 건 처음 풀어서 미처 생각을 못함.
또 x, y가 위->아래/왼->오 라는걸 유념할 필요가 있다.. 가로 세로를 잘 생각해야 함
x y가 배열 밖으로 나가는 경우 반드시 고려할 것
x y 이왕이면 dx dy nx ny 사용에 익숙해지자
"""

## 정답

"""
DFS와 BFS의 차이 빼고는 내 풀이가 보통인 듯! 잘했다
"""