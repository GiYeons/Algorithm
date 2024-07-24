# 성적이 낮은 순서로 학생 출력하기
## 내 풀이 (풀이시간: 8분)
import sys

read = sys.stdin.readline
N = int(read())
dic = [read().split() for _ in range(N)]

def return_key(d):
  return int(d[1])

dic.sort(key=return_key)

for d in dic:
  print(d[0], end='')
"""
sort()의 key 사용법을 몰라서, 중단 후 다시 작성함.
"""
## 정답
import sys

read = sys.stdin.readline
N = int(read())
arr = []

for _ in range(N):
  data = read().split()
  arr.append((data[0], int(data[1])))

arr.sort(key = lambda student: student[1])

for a in arr:
  print(a[0], end='')