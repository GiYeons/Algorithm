# 곱하기 혹은 더하기 (풀이시간: 9분 30초)
## 내 풀이
S = input()
arr = []

for s in S:
  arr.append(int(s))

result = arr[0]
for n in arr[1:]:
  if result == 0 or n == 0 or result == 1 or n == 1:
    result += n
  else:
    result *= n

print(result)
"""
경우의 수를 생각하면서 풀었다. 피연산자 둘 중 하나가 0 또는 1이 아니면 무조건 곱하기가 이득이라고
생각했다. 0을 곱하면 0이 되고, 1을 곱하면 숫자가 유지되니까.
--아이디어--
for s in S 로 돌면서 리스트 append 할것
0부터 9가 주어진다
+ 아니면 x인데 숫자 사이에 넣을 수만 있음
그리고 순서대로 됨 
그럼 사실 무조건 곱하기가 되는게 좋지않나
근데 0일경우 +여야됨...1이어도 +
2부터는 *가 무조건 좋다

n n 
둘중하나라도 0이거나
하나라도 1이거나
둘다 0도 1도 아니면 곱하기가 좋다!

result = 일단 0 인덱스 빼두고
for  arr 하면서 1인덱스부터
	result가 0 1인지 보고 아니면 곱할것
"""

## 답
S = input()

result = int(S[0])

for n in S[1:]:
  n = int(n)
  if result <= 1 or n <= 1:
    result += n
  else:
    result *= n

print(result)
"""
리팩토링한 코드. 굳이 미리 S를 int array로 변환해두지 않아도 String 자체로 반복문을
돌리면 된다. 또 조건문을 간결하게 줄이는 방법이 있었다.
"""