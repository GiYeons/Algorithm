# 숫자 카드 게임
## 내 풀이
import sys
import time

start = time.time()


N, M = map(int, input().split())
read = sys.stdin.readline
cards = [list(map(int, read().split())) for _ in range(N)]


for i in range(N):
  cards[i].sort()

mins = []
for i in range(N):
  mins.append(cards[i][0])


end = time.time()

print(max(mins))
print("time: ", "%.5f" %(end-start))

"""
원래 아이디어는 정말 단순하게, 모든 행에서 제일 작은 것을 골라내서 정렬된 리스트를 만든 다음
가장 큰 수를 뽑고, 그걸 포함된 행을 찾는 거였다. 그런데 너무 복잡하게 생각하는 것 같아서
모든 행을 처음부터 정렬한 뒤 0번 인덱스에 해당하는 숫자 중 제일 큰 걸 찾기로 했다.
"""

## 답안
import sys

N, M = map(int, input().split())
read = sys.stdin.readline

max_value = -1

for i in range(N):
  data = list(map(int, read().split()))
  min_value = min(data)

  max_value = max(min_value, max_value)

print(max_value)
  

"""
줄마다 입력받아 확인한다. 현재 줄에서 가장 작은 수를 찾고, 가장 작은 수 중에서 가장 큰 수를
찾는다.
"""