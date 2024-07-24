# 1개미 전사
## 내 풀이 (풀이시간: 기권)

"""
15분째에서 해설을 봤는데도 아이디어를 떠올리지 못해 포기함.
"""

## 정답
import sys

read = sys.stdin.readline
N = int(input())
arr = list(map(int, read().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, N):
  d[i] = max(d[i - 1], d[i - 2] + arr[i])

print(d[N - 1])

"""
왼쪽부터 차례대로 식량창고를 턴다고 가정하여 점화식을 세운다. 특정한 i번째 식량창고에 대해
털지 안 털지의 여부를 결정할 때, 2가지 경우만 확인하면 된다.
1. (i-1)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 없다.
2. (i-2)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 있다.
따라서 1번과 2번 중 더 많은 식량을 얻을 수 있는 경우를 선택하면 된다.
점화식은 다음과 같다.
a i = max(a i-1, a i-2 + k i)
"""