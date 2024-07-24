# 미래 도시
## 내 풀이 (풀이시간: 40분, 실패)
import sys
import heapq
read = sys.stdin.readline
INF = int(1e9)

N, M = map(int, read().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  a, b = map(int, read().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

X, K = map(int, read().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
      
    for node in graph[now]:
      cost = dist + node[1]
      if distance[now[0]] > distance[node] + 1:
        distance[now] = distance[node] + 1


dijkstra(K)

if distance[X] == INF:
  print(-1)
else:
  print(distance[X])
  
"""
첫 최단경로 문제 풀이라 다익스트라를 구현하는 것 자체가 쉽지 않았다. 기억나는 대로 쥐어짜는
것만이라도 일단 해봤다.
"""

## 정답
import sys
read = sys.stdin.readline
INF = int(1e9)

N, M = map(int, read().split())
# 2차원 리스트(그래프 표현) 생성 및 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자신으로 가는 비용 0으로 초기화
for a in range(1, N + 1):
  for b in range(1, N + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선의 정보 입력받아 그 값으로 초기화
for _ in range(M):
  # A와 B가 서로에게 가는 비용은 1로 설정
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

X, K = map(int, read().split())

# 점화식에 따라 플로이드 알고리즘 수행
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우
if distance >= INF:
  print("-1")
else:
  print(distance)
  
"""
1번 노드에서 X를 거쳐 K까지 가는 최단 거리는 (1번 노드에서 X까지의 최단 거리+X에서 K까지의
최단 거리)이다!
N의 범위가 100 이하로 매우 한정적이므로 구현이 간단한 플로이드 알고리즘을 활용해도 된다. 
"""