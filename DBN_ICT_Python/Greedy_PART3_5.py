# 볼링공 고르기 (풀이시간: 7분 30초)
## 내 풀이
import sys
read = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, read().split()))
weight.sort()

result = 0
for i in range(len(weight)):
  a = weight[i]
  for j in range(i + 1, len(weight)):
    b = weight[j]
    if a != b:
      result += 1

print(result)

"""
어떻게 고르든 서로 무게가 다르게 선택하면 된다
일단 정렬을 하고싶음..오름차순으로
A가 먼저 볼링공을 고르면 B가 무게가 다른 볼링공을 골라야함
번호가 다르기만하면 무게는 같아도 상관없어...

일단 정렬
for 볼링공 리스트:
	a = 볼링공[i]
	for i+1부터:
		b = 볼링공[j]
		만약 a b가 무게가 다르면
		result += 1
"""

## 답
import sys
read = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, read().split()))

arr = [0] * 11

for w in weight:
  # 각 무게에 해당하는 볼링공 개수 카운트
  arr[w] += 1

result = 0
# 1부터 m까지의 각 무게에 대해 처리
for i in range(1, M + 1):
  N -= arr[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += arr[i] * N  # B가 선택하는 경우의 수와 곱하기

print(result)

"""
내 풀이도 틀리지는 않았겠지만 더 효율적으로 풀 수 있는 방법이 있다.
먼저 무게마다 볼링공이 몇 개 있는지를 계산한다. 이때 A가 특정한 무게의 볼링공을 선택했을 때
이어서 B가 볼링공을 선택하는 경우를 차례대로 계산하여 문제를 해결한다. 예를 들어
무게가 1인 볼링공: 1개
무게가 2인 볼링공: 2개
라면 A가 무게가 1인 공을 선택할 때의 경우의 수는
1(공의 개수) * 4(B가 선택하는 경우의 수) = 4가지 경우이다.

볼링공의 무게가 1부터 10까지만 존재할 수 있으므로 하나의 리스트 변수를 선언하여 각 무게별
볼링공 개수를 기록할 수 있다.
"""