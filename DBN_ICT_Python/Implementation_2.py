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
  