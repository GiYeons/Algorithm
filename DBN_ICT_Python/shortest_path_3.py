# 전보
## 내 풀이 (풀이시간: 29분)
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, read().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  X, Y, Z = map(int, read().split())
  graph[X].append((Y, Z))

distance = [INF] * (N + 1)

def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
      continue

    for node in graph[now]:
      if distance[node[0]] > dist + node[1]:
        distance[node[0]] = dist + node[1]
        heapq.heappush(q, (distance[node[0]], node[0]))


dijkstra(C)


sum_of_city = -1
max = 0
for i in distance:
  if i < INF:
    sum_of_city += 1
    if max < i:
      max = i

print(sum_of_city, max)

"""
다익스트라 알고리즘을 거의 수정할 필요가 없어 쉽게 풀었다. 아래는 변수명 등 사소한 부분만
리팩토링한 코드다.
"""

## 정답
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, read().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  X, Y, Z = map(int, read().split())
  graph[X].append((Y, Z))

distance = [INF] * (N + 1)

def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
      continue

    for node in graph[now]:
      cost = dist + node[1]
      if distance[node[0]] > cost:
        distance[node[0]] = cost
        heapq.heappush(q, (cost, node[0]))


dijkstra(C)


sum_of_city = -1
max_distance = 0
for d in distance:
  if d < INF:
    sum_of_city += 1
    max_distance = max(max_distance, d)

print(sum_of_city, max_distance)