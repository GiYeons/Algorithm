# 문자열 재정렬 (풀이시간: 9분, 실패)
## 내 풀이
S = input()

num = 0
str = ""
for s in S:
  if int(s) >= 0 and int(s) <= 9:
    num += int(s)
  else:
    str += s

print(str + str(num))

"""
문자열 원소를 하나씩 살펴보며 알파벳인지 확인하고, 나중에 알파벳과 숫자를 더하려고 했다.
그러나 문자열 지식의 부재로 풀지 못하는 문제 같아서 빨리 답지를 보기로 한다.
"""

## 정답
S = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for s in S:
  # 알파벳인 경우 결과 리스트에 삽입
  if s.isalpha():
    result.append(s)
  # 숫자는 따로 더하기
  else:
    value += int(s)

# 알파벳을 오름차순으로 정렬
result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))

"""
isalpha() 함수의 존재를 몰랐고, 숫자가 없는 경우를 고려하지 못했다.
"""