# 특정 거리의 도시 찾기 (풀이시간: 약 45분, 실패)
## 내 풀이
"""
BFS로 풀수있지않을까
일단 입력을 받아서 2차원 그래프를 만든다..

x로부터 거리를 기록하는 그래프를 하나더 만들고
graph[x][] 를 루프 돌려서 +1을 함
방문처리하고 deque에 넣어
첫번째 루프에선 +1이 되겠지
그리고 이제부턴..deque에 있는 노드들을 하나씩 뽑아서
또 그 노드에서 갈 수 있는 다른 노드들을 루프 돌리는거야....
+1을 하기 전에 K인지 확인하고 K라면 컨티뉴
이때 +1를 하고 K가 됐는지 확인한다
만약 K가 됐으면 result에 푸쉬
그렇게 모든 루프를 끝내고나면..
result가 0이라면 -1 출력 아니라면 리스트 출력
----------
아이디어는 대충 비슷했는데 논리적으로 정리가 어려웠던 것 같다.
"""
import sys
from collections import deque
INF = -1e9

read = sys.stdin.readline
N, M, K, X = map(int, read().split())
graph = [[INF] * (N+1)] * (N+1)
visited = [-1] * (N + 1)

for _ in range(M):
  A, B = map(int, read().split())
  graph[A][B] = 1

result = []
distance = [[0] * (N+1)] * (N+1)

queue = deque([X])
while queue:
  now = queue.popleft()
  visited[now] = 1
  
  for i in range(1, N+1):
    if graph[now][i] == 1 and not visited[i]:
      if distance[now][i] == K:
        continue
      distance[now][i] += 1

      if distance[now][i] == K:
        result.append(i)
        continue

      queue.append(i)

print(result)

## 정답
