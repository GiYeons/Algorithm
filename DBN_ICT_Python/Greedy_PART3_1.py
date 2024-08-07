# 모험가 길드 (풀이시간: 15분, 실패)
## 내 풀이
"""
최대 그룹.....그룹이 최대려면 한 그룹당 인원이 최대한 적어야함
그러려면 공포도가 높은 애를 버리거나 어케 처리해야
정렬해서 적은 애들끼리 최대한 묶으면 되지않나?
까지 생각했지만 그룹을 어떻게 묶는지 모르겠다.
"""

## 답
N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가 수

for i in data:
  count += 1
  if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
    result += 1
    count = 0

print(result)

"""
앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는
공포도'보다 크거나 같다면 그룹으로 설정한다.
"""