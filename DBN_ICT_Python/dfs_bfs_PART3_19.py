# 연산자 끼위 넣기 (풀이시간: 약 20분, 포기)
## 내 풀이
    
"""
DFS로 순서대로 트리 타고 내려가면서 모든 경우의 수 할 수 있도록 구현하고 싶었는데
머리가 안돌아가서 못하겠다..
"""

## 정답 
import sys

N = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최솟값과 최대값
min_value = 1e9
max_value = -1e9

def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자 다 사용한 경우 최솟값과 최댓값 업데이트
  if i == N:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, int(now / data[i]))
      div += 1

dfs(1, data[0])

print(max_value)
print(min_value)
"""
흐름을 잘 이해할 것.
"""