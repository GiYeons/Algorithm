# 럭키 스트레이트 (풀이시간: 7분 30초)
## 내 풀이
N = input()

left = 0
right = 0
for i in range(len(N) // 2):
  left += int(N[i])
  right += int(N[-(i + 1)])

print("LUCKY" if left == right else "READY")

"""
최대 자릿수가 8이므로, 단순히 점수를 반으로 쪼개서 하나하나 더해도 문제 없다고 생각했다.
"""

## 정답
N = input()

summary = 0
length = len(N)

for i in range(length // 2):
  summary += int(N[i])

for i in range(length // 2, length):
  summary -= int(N[i])
  

print("LUCKY" if summary == 0 else "READY")

"""
for 문을 두번 돌리며 결과값을 더했다가 빼는 아이디어가 신선하다.
일단 기억해둘 것.
"""