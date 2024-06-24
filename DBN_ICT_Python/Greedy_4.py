# 1이 될 때까지
## 내 풀이 1
N, K = map(int, input().split())

result = 0

while N > 1:
  if N % K == 0:
    N /= K
  else:
    N -= 1
  result += 1

print(result)

"""
K로 나누는 것이 무조건 좋은 거라고 자연스럽게 생각했는데, 다음에는 왜 그게 최적이라고 생각했는지
머릿속에서 검증하는 연습을 해야겠다. 최대한 많이 나누는 것이 좋으므로 먼저 나누어떨어지는지
확인하고, 가능하면 나눈 다음 안되면 1을 빼도록 했다.
교재에 따르면 더 정확한 표현은 1.N이 K의 배수가 될 때까지 1을 빼고 2.N을 K로 나누는 것이다.
다만 이는 N의 범위가 10만 이하이기 때문에 가능한 단순 풀이로, 100억 이상이 되면
N이 K의 배수가 되도록 한 번에 빼야 한다.
"""

# 내 풀이 2
N, K = map(int, input().split())

result = 0

while N >= K:
  if N % K == 0:
    N //= K
    result += 1
  else:
    result += N % K
    N -= N % K

  
print(result)
result += N - 1

print(result)