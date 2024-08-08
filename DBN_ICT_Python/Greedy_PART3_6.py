# 무지의 먹방 라이브 (풀이시간: 30분, 실패)
## 내 풀이
def solution(food_times, k):
    idx = 0
    
    for i in range(k):
        if idx >= len(food_times):
            idx = 0
            
        if food_times[idx] > 0:
            food_times[idx] -= 1
            idx += 1
        else:
            while food_times[idx] == 0:
                idx += 1
                if idx >= len(food_times):
                    idx = 0
            food_times[idx] -= 1
            idx += 1
            
    
    answer = idx
    return answer

"""
--아이디어--
for k:
    자 인덱스가 있지?
    이게 지금 먹어야되는 음식임
    만약 현재 인덱스가 ft len 보다 크거나 같다면:
        idx = 0
        현재 인덱스가 0이 아니면:
            ft에서 inx 번째 인덱스 -1를 한다
        0이라면:
            0이 아닌 인덱스에 도달할때까지 +1로 while을 돌린다.돌리는데
            매번 ft len과 크거나 같으면 idx= 0으로
            0이 아닌 인덱스를 찾았다면 -1

이러고 idx 가 정답
"""

## 답
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) >= k:
        return -1
    
    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0   # 먹기 위해 사용한 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재의 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1     # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1])    # 음식 번호 기준 정렬
    return result[(k - sum_value) % length][1]

"""
아이디어는 쉬운데 소스코드가 어렵다. 시간이 적게 걸리는 탐욕적 접근 방식으로 해결할 수 있다.
모든 음식을 시간 기준으로 정렬한 뒤에, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을
이용하면 된다. 이를 위해 우선순위 큐를 이용하여 구현할 수 있다.
- 1번 음식: 8초 소요
- 2번 음식: 6초 소요
- 3번 음식: 4초 소요
0. 모든 음식을 우선순위 큐에 삽입한다.
1. 첫 단계에서는 가장 적게 걸리는 음식인 3번 음식을 뺀다. 다만 음식이 3개 남아 있으므로
3(남은 음식의 개수) * 4(음식을 먹는 데 걸리는 시간) = 12를 빼야 한다. 다시 말해
3번 음식을 다 먹기 위해서는 12초가 걸린다. 결과적으로 전체 남은 시간이 15초에서 3초로 줄어든다.
2. 전체 남은 시간은 3초이고, 이번 단계에서는 2번 음식을 빼야 한다. 전체 음식이 2개 남았으므로
이번 단계에서 뺄 시간은 2(남은 음식의 개수) * 6(2번 음식을 다 먹는 시간) = 12초가 된다.
현재 남은 시간이 3초인데 이는 12보다 작으므로 빼지 않도록 한다.
따라서 다음으로 먹어야 할 음식으 번호를 출력하면 되는데, 남은 시간이 3초이므로 4번째 음식 번호를
출력하면 된다.
"""