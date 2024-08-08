# 기둥과 보 설치 (풀이시간: 약 30분, 포기)
## 내 풀이

"""
이걸 어떻게 풀지....로직 생각하다 포기했다
---------
기둥: 바닥 위, 보의 한쪽 끝 위, 기둥 위
보: 한쪽 끝이 기둥 위, 또는 양쪽 끝이 달른 보와 연결
규칙에 맞게 설치 또는 삭제해야 한다
bulid_frame: x, y, a(0 기둥 1 보), b(삭제 0 설치 1)
바닥에 보 설치X 벽면 벗어남 X
좌표를 기준으로 보는 오른쪽, 기둥은 위쪽으로 설치
구조물이 겹치거나 없는 구조물을 삭제하는 경우 없음 -> 맵을 벗어나는지, 규칙에 맞는지만 신경쓴다

return은 각 구조물의 좌표 x y a .. 순서대로 오름차순 정렬해서
----
한 좌표당 기둥1 보 1 설치 가능 
기둥만 1 보만 2 둘다 3
NxN 맵 만들어두기

build_frame를 하나씩 for:
    하나씩 꺼내서 좌표를 확인한다.. 
    설치다:
    기둥인지 보인지 확인한다
    만약 기둥이라면:
        맵을 벗어나는가? 바닥 위(y좌표 0)거나 보의 한쪽 끝 위(2거나 x-1이 2인가), 기둥 위(y-1이 1)인가?
    보라면:
        맵을 벗어나는가? 바닥(y좌표 0)인가? 한쪽 끝이 기둥 위(1이거나 x+1이 1), 또는 양쪽 끝이 다른 보와 연결(2이고 x+1도 2)
    삭제라면:
        만약 기둥이라면:
            일단 삭제한다...삭제하고 체크한다
    
answer는 마지막에 맵을 쭉 돌면서 추가하도록 한다
"""

## 정답
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False    # 아니라면 거짓 반환
        elif stuff == 1:    # 설치된 것이 '보' 인 경우
            # 한쪽 끝부분이 '기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결' 이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False    # 아니라면 거짓 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:   # 작업(frame)의 개수는 최대 1000개
        x, y, stuff, operate = frame
        if operate == 0:    # 삭제하는 경우
            answer.remove([x, y, stuff])    # 일단 삭제를 해본 뒤에
            if not possible(answer):    # 가능한 구조물인지 확인
                answer.append([x, y, stuff])    # 가능한 구조물이 아니라면 다시 설치
        if operate == 1:    # 설치하는 경우
            answer.append([x, y, stuff])    # 일단 설치를 해본 뒤에
            if not possible(answer):    # 가능한 구조물인지 확인
                answer.remove([x, y, stuff])    # 가능한 구조물이 아니라면 다시 제거
                
    return sorted(answer)   # 정렬된 결과 반환
    
"""
전체 명령의 개수를 M이라고 할 때 M은 총 1,000개 이하이므로, 시간 복잡도 O(M^2)로
해결하는 것이 이상적이다. 그러나 본 문제의 시간 제한은 5초로 넉넉하므로 O(M^3)이아도 무방하다.
가장 간단한 방법은 설치 및 삭제 연산을 요구할 때마다 일일이 전체 구조물을 확인하며 규칙을
확인하는 것이다. 위 소스코드에서는 possible() 메서드를 이용하여 현재의 구조물이 정상인지
체크하고, 정상이 아니라면 현재의 연산을 무시한다.
"""