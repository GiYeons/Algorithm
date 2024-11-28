# 바이러스 (풀이시간: 약 13분, 성공)
## 내 풀이
import sys
from collections import deque

read = sys.stdin.readline
N = int(read())
M = int(read())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
  A, B = map(int, read().split())
  graph[A].append(B)
  graph[B].append(A)


def bfs():
  visited[1] = True
  queue = deque([1])
  result = 0

  while queue:
    now = queue.popleft()
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)
        result += 1

  return result

print(bfs())

"""
그냥 BFS 문제... 별다른 변형도 없다 그냥 BFS 그대로 쓰면 됨
"""

## 정답
import sys
from collections import deque

read = sys.stdin.readline
N, M, V = map(int, read().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
  A, B = map(int, read().split())
  graph[A].append(B)
  graph[B].append(A)

for i in range(1, N + 1):
  graph[i].sort()

def dfs(start):
  visited[start] = True
  print(start, end=' ')
  
  for next_node in graph[start]:
    if not visited[next_node]:
      dfs(next_node)

dfs(V)
print()

visited = [False] * (N + 1)

queue = deque([V])
visited[V] = True

while queue:
  now = queue.popleft()
  print(now, end=' ')

  for next in graph[now]:
    if not visited[next]:
      queue.append(next)
      visited[now] = True
"""
과정이 헷갈리고 이해가 안 되면 손으로 직접 그래프를 그려보는 게 좋을 듯.
"""