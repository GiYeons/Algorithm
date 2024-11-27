# DFS와 BFS (풀이시간: 약 37분, 성공)
## 내 풀이
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
  if visited[start] == True:
    return

  visited[start] = True
  print(start, end=' ')
  for next_node in graph[start]:
    if not visited[next_node]:
      dfs(next_node)

dfs(V)
print()

visited = [False] * (N + 1)

queue = deque([V])

while queue:
  now = queue.popleft()
  if visited[now]:
    continue

  visited[now] = True
  print(now, end=' ')

  for next in graph[now]:
    if not visited[next]:
      queue.append(next)

"""
DFS/BFS는 왜 풀때마다 까먹는지 모르겠다. 정리본 슬쩍 보고 풀었다.
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