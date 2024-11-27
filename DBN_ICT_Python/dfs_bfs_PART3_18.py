# 괄호 변환 (풀이시간: 약 22분, 실패)
## 내 풀이
def solution(p):
    return dfs(p)

def isRightStr(str):
    count = 0
    for s in str:
        if s == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    
    if count != 0:
        return False
    else:
        return True
    
def dfs(str):
    if str == "":
        return ""
    
    left = right = 0     # 왼오 괄호 개수 카운트
    for s in str:
        if s == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break
    
    u = str[:left + right]
    v = str[left + right:]
    
    if isRightStr(u):
        return u + dfs(v)
    else:
        result = "(" + dfs(v) + ")"
        temp = u[1:-1]
        
        # 괄호 뒤집기
        for t in range(len(temp)):
            if temp[t] == "(":
                temp.replace("(", ")")
            else:
                temp.replace(")", "(")
                
        return result + temp
    
"""
괄호를 바꾸는 등의 로직은 생각이 나지 않았지만 전체적인 알고리즘은 그냥 서술된 바와 똑같이
구현하면 되는 것 같아서 그 부분이라도 작성했다.

시간제한 후 생각해본 isRightStr 로직:
count 변수 선언. 괄호를 하나씩 확인하면서 left일땐 +하고 right일땐 -한다.
만약 count가 한번이라도 -상태가 되면 right괄호가 더 많다는 것이고, 옳은 괄호가 아니다.
str을 다 돌았는데 count가 0이 아니라면 그 또한 옳은 괄호가 아니다!
--------------
수정!
에러 해결 후 실행했더니 테스트 2개만 통과했다.
"""

## 정답 
def balanced_index(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# "올바른 괄호 문자열"인지 판단 
def check_proper(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:  # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True     # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ""
    if p == "":
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니면 아래의 과정을 수행
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])   # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer
"""
구현을 위한 알고리즘은 문제에 제시되어 있으므로 재귀 함수를 이용해 실수 없이 구현할 수 있으면
문제를 해결할 수 있다.
내가 작성한 코드와 알고리즘은 같은데 어느 부분에서 틀린 건지 체크해 봐야겠다.
"""