# 자물쇠와 열쇠 (풀이시간: 22분, 실패)
## 내 풀이
def rotate(key):
    row = len(key)
    col = len(key[0])
    new_key = [[0] * row] * col
    
    for i in range(row):
        for j in range(col):
            new_key[j][-(j + 1)] = key[i][j]
            
    return new_key
            
            

def solution(key, lock):
    answer = True
    new_key = rotate(key)
    return new_key
    
"""
rotate 구현만이라도 해보려고 했는데 그것부터가 잘 되지 않는다.
"""

## 정답
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])   # 열 길이 계산
    result = [[0] * n for _ in range(m)]    # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result
    
# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

"""
제시한 자물쇠와 열쇠의 크기는 20x20보다 작다. 크기가 20x20인 2차원 리스트에 있는 모든
원소에 접근할 때는 400만큼의 연산이 필요하다. 일반적인 코테 채점 환경이라면 완전 탐색을
이용해 열쇠를 회전하거나 이동시켜서 전부 끼워보는 작업이 가능하다.
탐색을 수월하게 하기 위해 자물쇠 리스트의 크기를 3배 이상으로 변경하면 편리하다. 자물쇠는
크기를 키운 리스트의 중앙 부분으로 옮긴다. 그리고 왼쪽 위부터 열쇠 배열을 한 칸씩 이동하며
차례대로 모든 홈을 채울 수 있는지 확인한다. 자물쇠 리스트에 열쇠 리스트의 값을 더한 뒤
자물쇠 부분의 모든 값이 1인지 확인하면 된다.
"""