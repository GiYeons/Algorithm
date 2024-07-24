# 부품 찾기
## 내 풀이 (풀이시간: 15분)
import sys

read = sys.stdin.readline
N = int(input())
arr = list(map(int, read().split()))
M = int(input())
order = list(map(int, read().split()))

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

result = []
for num in order:
  if num > 1000000:
    result.append("no")
  elif binary_search(arr, num, 0, N - 1) == True:
    result.append("yes")
  else:
    result.append("no")

print(*result)

"""
기본적인 이진탐색 알고리즘으로 풀면 될 거라고 생각했다. 다만 이진탐색으로 문제를 풀려면 먼저
정렬을 해야한다는 걸 잊었다.

부품을 찾는 과정에서 O(MlogN)의 연산이 필요하다. M이 최대 100,000이고 N이 최대
1,000,000이므로 이론상 최대 200만번의 연산이 이루어진다. 오히려 N개의 부품을 정렬하기 위해
O(NlogN)이 요구되므로 이론적으로 약 2000만번의 연산이 요구된다. 결과적으로 이진 탐색을
활용할 때 시간 복잡도는 O((M+N)logN)이다.
이 문제는 여러 풀이 방법이 있을 수 있는데, 하단에 3가지 모두 기재한다.
"""
## 정답 1 (이진 탐색)
import sys

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False


read = sys.stdin.readline
N = int(input())
arr = list(map(int, read().split()))
M = int(input())
order = list(map(int, read().split()))
arr.sort()

for num in order:
  if num > 1000000:
    print("no", end=' ')
  elif binary_search(arr, num, 0, N - 1) == True:
    print("yes", end=' ')
  else:
    print("no", end=' ')

print(*result)

"""
모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤에, 리스트의 인덱스에 직접 접근하여
특정한 부품이 매장에 존재하는지 확인한다.
"""
## 정답 2 (계수 정렬)
import sys

read = sys.stdin.readline
N = int(input())
arr = [0] * 1000000

# 가게에 있는 부품 전체를 입력받아 기록
for i in read().split():
  arr[int(i)] = 1

M = int(input())
order = list(map(int, read().split()))

for o in order:
  if arr[o] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')
    
"""
단순히 특정한 수가 한 번이라도 등장했는지 검사하면 되므로 set() 함수를 이용해서 문제를
해결할 수 있다. set() 함수는 특정한 데이터가 존재하는지 검사할 때 효과적이다.
"""
## 정답 3 (set() 함수 이용)
import sys

read = sys.stdin.readline
N = int(input())
arr = set(map(int, read().split()))

M = int(input())
order = list(map(int, read().split()))

for o in order:
  if o in arr:
    print("yes", end=' ')
  else:
    print("no", end=' ')