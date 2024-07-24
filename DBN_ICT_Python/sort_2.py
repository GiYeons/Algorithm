# 위에서 아래로
## 내 풀이 (풀이시간: 3분 30초)
import sys

N = int(input())
read = sys.stdin.readline
list = [int(read()) for _ in range(N)]

list.sort(reverse=True)
print(*list)