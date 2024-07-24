# 떡볶이 떡 만들기
## 내 풀이 (풀이시간: 40분)
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
list = list(map(int, read().split()))
print(list)

sum_res = sum(list)

def binary_search(start, end):
  while start <= end:
    mid = (end + start) // 2
    total = sum_res - (mid * N)
    print(mid, total)
    if total == M:
      return mid
    elif total < M:
      end = mid - 1
    else:
      if sum_res - (mid + 1) * N > M:
        start = mid + 1
      else:
        return mid

result = binary_search(0, max(list))
print(result)
"""
연산자를 헷갈리는 등 사소한 문제가 계속 있었다. 결과값이 답과 다르게 나왔는데, 절단기 높이보다
짧은 떡의 경우 절단하지 않는다는 조건을 고려하지 않아 틀린 답이 나온 듯하다.
아이디어를 떠올리는 데 급급해서 모든 조건을 고려하지 못했다.

--아이디어--
모든 떡에서 H를 제했을 때 그 총합이 M보다 커야함
모든 떡을 더하고 H*N을 제했을때 총합이 M보다 크면서...  (H+1)*N은 M보다 작아야함
그럼 이 H는 어떻게 구해야하나 이 조건에서 

0에서 10억까지 이진탐색을 돌린다
start end
mid 값으로 떡 더하고 제하기 계산을 했을때 총합이 M보다 작으면:
	절단을 더 작게 해야함. 즉 end에 mid를 넣는다
만약에 M보다 크면:
	H+1*N을 해봤는데 M보다 작은지 확인한다. 만약 크다면:
	start = mid+1 하고 다시 돌린다
	만약 작다면:
	그걸 반환
"""
## 정답
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, read().split()))

start = 0
end = max(arr)

result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for a in arr:
    # 잘랐을 때 떡의 양 계산
    if a > mid:
      total += a - mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)
  if total < M:
    end = mid - 1
  else:
    result = mid # 최대한 덜 잘랐을때가 정답이므로 여기서 result 기록
    start = mid + 1

print(result)
"""
전형적인 이진 탐색 문제이자 파라메트릭 서치 문제. 파라메트릭 서치는 최적화 문제를 결정 문제(
예 혹은 아니오로 답하는 문제를 의미함)로 바꾸어 해결하는 기법이다. '원하는 조건을 만족하는 가장
알맞은 값을 찾는 문제'에 주로 이 기법을 사용한다. 예를 들어 범위 내에서 조건을 만족하는
가장 큰 값을 찾는 최적화 문제는 이진 탐색으로 결정 문제를 해결하며 범위를 좁혀갈 수 있다.
코테에서 이 유형의 문제는 주로 이진 탐색을 이용하여 해결한다.
풀이 아이디어는 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정하는 것이다.
'현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인 후에 조건의 만족 여부에 따라
탐색 범위를 좁혀서 해결할 수 있다.
절단기의 높이는 0에서 10억까지인데, 이처럼 큰 수를 보면 이진 탐색을 떠올려야 한다.
높이 범위가 한정적이었다면 순차 탐색으로도 해결할 수 있으나 현재 기준으로는 그럴 수 없다.

높이 H를 이진 탐색으로 찾는다면 대략 31번 만에 모든 경우의 수를 고려 가능하다. 이때
떡의 개수 N이 최대 100만 개이므로 절단기 높이를 바꾸면서 모든 떡의 길이를 체크하는 경우
최대 3000만번 연산으로 문제를 풀 수 있다.
절단기의 높이는 떡의 최대 길이보다 짧거나 같다. 즉 0<=H<=떡의 최대 높이이다.
"""