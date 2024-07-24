# 바닥 공사
## 내 풀이 (풀이시간: 약 1시간)
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(read()) for _ in range(N)]

d = [0] * 10001

# 기본 화폐 인덱스 초기화
for a in arr:
  d[a] = 1

result = 0

for i in range(1, M + 1):
  comp_list = []
  for a in arr:
    if i - a > 0 and d[i - a] > 0:
      comp_list.append(d[i - a] + 1) 

  if comp_list:
    d[i] = min(comp_list)

if d[M] > 0:
  print(d[M])
else:
  print(-1)
  
"""
--아이디어--
i의 최소개수를 구하기 위해서는.....
어떻게 보면 i보다 작은 가치들의 합...인거잖아
점화식..... 

그러면 i는 어떻게 만들어지느냐
3 5 7이라는 화폐단위가 있을때
min (i - 3, i - 5, i - 7) 이 셋중에 젤 작은거에 +하면 되는거임
근데 만약에 이게 인덱스를 벗어난다거나... 해당 인덱스가 0이면 없는 거지...
min 안에 들어가는 모든 값이 인덱스를 벗어나거나 0이라면...

min (i - 3, i - 5, i - 7) 이걸 어떡하지? 저 3 5 7 리스트는 배열로 받았는데
N가지 종류인건 아니까...
0~N-1까지 돌면서 arr
"""

## 정답
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(read()) for _ in range(N)]

# DP 테이블 초기화
d = [10001] * (M + 1)

# 보텀업
d[0] = 0
for i in range(N):
  for j in range(arr[i], M + 1):
    if d[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j - arr[i]] + 1)

if d[M] == 10001:
  print(-1)
else:
  print(d[M])
  
"""
그리디에서 다룬 거스름돈 문제와 거의 동일하지만, 화폐 단위에서 큰 단위가 작은 단위의 배수가
아니라는 점만 다르다. 그렇기 때문에 가장 큰 화폐 단위부터 처리하는 방식으로는 해결할 수 없고
다이나믹을 활용해야 한다.
적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾는다.
금액 i를 만들 수 있는 최소한의 화폐 개수를 a, 화폐의 단위를 k라고 했을 때 점화식은 다음과
같다.
a i-k 를 만드는 방법이 존재하는 경우, a i = min(a i, a i-k + 1)
a i-k 를 만드는 방법이 존재하지 않는 경우, a i = 10001
이 점화식을 모든 화폐 단위에 적용한다.
"""