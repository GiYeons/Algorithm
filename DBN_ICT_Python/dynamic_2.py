# 1로 만들기
## 내 풀이 (풀이시간: 23분+a)
X = int(input())

arr = [0] * 30001

arr[1], arr[2], arr[3], arr[4], arr[5] = 0, 1, 1, 2, 1

for i in range(6, X + 1):
  cnt = 0
  temp = i
  while temp % 5 != 0 and temp % 3 != 0 and temp % 2 != 0:
    cnt += 1
    temp -= 1
    
  if temp % 5 == 0:
    arr[i] = arr[i//5] + 1
  elif temp % 3 == 0:
    arr[i] = arr[i//3] + 1
  else:
    arr[i] = arr[i//2] + 1
  arr[i] += cnt

print(arr[:X+1])

"""
처음에 이 문제가 왜 다이나믹이고 어떻게 풀 수 있는지 전혀 파악하지 못했다.
위는 문제 해설을 열어보고 작성한 코드이다. 처음 주어진 몇 개의 초기값을 고정해두고
해당 값으로 나머지 값을 구하려고 했다.
"""
## 정답
X = int(input())

d = [0] * 30001

# 보텀업 방식
for i in range(2, X + 1):
  # 현재의 수에서 1을 빼는 경우
  d[i] = d[i-1] + 1
  # 현재의 수가 2로 나누어 떨어지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  # 현재의 수가 3로 나누어 떨어지는 경우
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  # 현재의 수가 5로 나누어 떨어지는 경우
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[X])

"""
점화식은 다음과 같다. a i = min(a i-1, a i/2, a i/3, a i/5) + 1
다이나믹 방법으로 풀고 싶다면 일단 초기값이 주어지는지, 그 초기값으로 상위 값들을 구할 수 있는지
생각해보면 될 것 같다.
"""