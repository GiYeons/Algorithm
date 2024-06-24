# 큰 수의 법칙
## 내 풀이
import sys

N, M, K = map(int, input().split())

read = sys.stdin.readline
list = list(map(int, read().split()))

answer = 0

while M > 0:

  fir_max = max(list)
  
  if M >= K + 1:
    
    answer += fir_max * K
    new_list = list.copy()
    new_list[new_list.index(fir_max)] = -1
    sec_max = max(new_list)
    answer += sec_max
    M -= K + 1
    
  elif M == K:
    answer += fir_max * K
    M -= K
    
  else:
    answer += fir_max * M
    M -= M

print(answer)

"""
입력:
5 8 3
2 4 5 4 6
--
실행시간: 0.00001 sec
--아이디어--
첫번째로 큰 수와 두번째로 큰 수만 필요하다고 생각했다. 첫번째 큰 수를 K번 더하고,
두번째로 큰 수를 1번 더한다. 이를 M번 반복한다.
여기까지는 생각했는데, 반복문을 돌리기 전에 두 숫자를 빼놓는다는 생각을 못했다.
그리고 가장 큰 수를 구한다고 해서 max를 사용할 생각밖에 못했다.
그리디 문제는 정렬과 함께 사용될 때가 많다는 것... 기억하자.
"""


## 정답1
import sys

N, M, K = map(int, input().split())

read = sys.stdin.readline
list = list(map(int, read().split()))

list.sort()
first = list[N - 1]
second = list[N - 2]

result = 0

while True:
  for i in range(K):
    if M <= 0:
      break
    result += first
    M -= 1

  if M <= 0:
    break
  result += second
  M -= 1

print(result)

"""
이 문제는 M이 10,000 이하이므로 이 방식으로 해결할 수 있지만, M의 크기가 100억 이상처럼
커진다면 시간초과를 받을 것이다. 수학적 아이디어를 이용해 효율적으로 문제를 해결해 보자.
"""

# 나의 2번째 풀이
import sys

N, M, K = map(int, input().split())

read = sys.stdin.readline
list = list(map(int, read().split()))

list.sort()
first = list[N - 1]
second = list[N - 2]

result = 0

loop_num = M // (K+1)
result += (first * K + second) * loop_num
result += first * (M % (K+1))

print(result)

"""
첫번째로 큰 수와 두번째로 큰 수를 더한 다음, 수열이 반복되는 횟수만큼 곱해준다.
그리고 남은 횟수만큼 첫번째로 큰 수를 더해준다.

* 교재 풀이
반복되는 수열의 특징을 이용하여 수식을 더 단순화할 수 있다. 가장 큰 수와 두번째로 큰 수가
더해질 때 특정한 수열 형태로 일정하게 더해진다. 위 예시에서는 [6, 6, 6, 5]가 반복된다.
이때 반복되는 수열의 길이는 (K+1)로 4이다. 따라서 M을 (K+1)로 나눈 몫이
수열이 반복되는 횟수이다. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
이때 M이 (K+1)로 나누어떨어지지 않는 경우도 있을 수 있으므로 그것도 추가로 더해준다.
"""

count = M // (K+1) * K
count += M % (K+1)

result += (count) * first
result += (m - count) * second