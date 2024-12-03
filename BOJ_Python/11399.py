# ATM (풀이시간: 약 20분, 성공)
## 내 풀이
n = int(input())
plist = list(map(int, input().split()))


plist.sort()
sum = 0
waiting = 0

for p in plist:
    sum += waiting + p
    waiting += p

print(sum)

"""
10분 이내로 풀 수 있는 문제였는데 아쉽다. 
머리로만 생각하지 말고 손으로 써보는 연습을 하자
"""

## 정답
"""
리스트의 0번째 수부터 x번째 수까지를 더해준다는 아이디어
"""