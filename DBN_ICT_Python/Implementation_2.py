# 왕실의 나이트
## 내 풀이 (풀이시간: 22분)
rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

input = input()
row, col = input[0], int(input[1]) - 1
row = rows.index(row)

row_move = [-2, -2, 2, 2, -1, 1, -1, 1]
col_move = [-1, 1, -1, 1, 2, 2, -2, -2]

result = 0

for i in range(len(row_move)):
  moved_row = row + row_move[i]
  moved_col = col + col_move[i]

  if not (moved_row < 0 or moved_row > 7 or moved_col < 0 or
  moved_col > 7):
      result += 1

print(result)

"""
입력이 숫자+알파벳으로 들어오므로 알파벳을 정수로 변환해야 했다. 원래는 아스키코드를 활용하려 했는데
사용법을 잊어버려서 급한 대로 하드코딩하여 사용했다. 나이트가 이동할 수 있는 경우의 수는 최대
8가지이므로 8가지 경우의 수를 모두 확인했다.
"""

## 답안
input = input()
row = int(input[1])
col = int(ord(input[0]) - ord('a')) + 1

steps = [
    (-2, -1), (-2, 1), (2, -1), (2, 1),
    (-1, -2), (-1, 2), (1, -2), (1, 2)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
        
print(result)