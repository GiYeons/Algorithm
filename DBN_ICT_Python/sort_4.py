# 두 배열의 원소 교체
## 내 풀이 (풀이시간: 5분 40초)
import sys

read = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
  A[i], B[i] = B[i], A[i]

print(sum(A))
"""
배열 A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때에만 교체를 해야 하는데,
그 조건을 미처 생각하지 못했다. 더 신중히 생각하고 검토할 것.
"""
## 정답
import sys

read = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break
    
print(sum(A))