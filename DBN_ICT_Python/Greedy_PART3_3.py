# 문자열 뒤집기 (풀이시간: 10분 30초)
## 내 풀이
S = input()

now = -1
one = 0
zero = 0
for s in S:
  s = int(s)
  if s == now:
    continue
    
  if s == 0:
    zero += 1
  else:
    one += 1
  now = s

print(min(one, zero))
"""
연속된 숫자를 그룹으로 묶어서 0과 1중 더 적은 수의 그룹 개수를 찾으려고 했다.
--아이디어--
행동이란 연속된 하나이상의 숫자를 뒤집는다
그냥 연속된 숫자가 몇개인지 보면 되는데
1이랑 0중에 연속된 숫자가 많은 그룹을 찾으면 되는듯
"""

## 답
S = input()

count0 = 0
count1 = 0

# 첫번째 원소 처리
if data[0] == '1':
  count0 += 1
else:
  count1 += 1

# 두번째 원소부터 모든 원소
for i in range(len(S) - 1):
  if S[i] != S[i + 1]:
    # 다음 수에서 1로 바뀌는 경우
    if S[i + 1] == '1':
      count0 += 1
    # 다음 수에서 0으로 바뀌는 경우
    else:
      count1 += 1

print(min(count0, count1))
"""
답이 더 어려운 것 같은데... 그래도 문자열에서 원소를 하나씩 확인하며 뒤의 원소와 비교하는 
스킬은 기억해두자.
"""