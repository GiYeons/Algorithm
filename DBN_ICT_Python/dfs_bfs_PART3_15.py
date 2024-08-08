# 특정 거리의 도시 찾기 (풀이시간: 약 9분, 실패)
## 내 풀이
"""
아침이라 머리가 안 돌아감... 다익스트라로 풀어야 되는 최단경로 문제 같은데 왜 DFS/BFS로
분류됐는지 이해를 못했다. 다익스트라를 까먹어서 다익스트라로도 풀 수가 없었음.
"""

## 정답
from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 모든 도로 정보 입력받기
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([X])
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순 출력
check = False
for i in range(1, N + 1):
  if distance[i] == K:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
  print(-1)
"""
그래프에서 모든 간선의 길이가 동일할 때는 BFS를 이용하여 최단 거리를 찾을 수 있다.
다시 말해 '모든 도로의 거리는 1'이라는 조건 덕분에 BFS로 해결할 수 있다는 것이다.
노드의 개수 N은 최대 300,000개이며 간선의 개수 M은 1,000,000개이므로 너비 우선 탐색을
이욯하여 시간 복잡도 O(N + M)으로 동작하는 소스코드를 작성할 수 있다.
먼저 특정 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤에
각 최단 거리를 하나씩 확인하여 그 값이 K인 경우 해당 도시 번호를 출력한다.
"""