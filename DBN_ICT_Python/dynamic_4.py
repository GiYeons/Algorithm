# 바닥 공사
## 내 풀이 (풀이시간: 18분, 기권)

"""
15분째에서 해설을 봤는데도 아이디어를 떠올리지 못해 포기함.
"""

## 정답
N = int(input())

# DP 테이블 초기화
d = [0] * 1001

# 보텀업
d[1] = 1
d[2] = 3
for i in range(3, N + 1):
  d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[N])

"""
1. 왼쪽부터 i-1까지 길이가 덮개로 이미 채워져 있으면 2x1의 덮개를 채우는 하나의 경우밖에
존재하지 않는다.
2. 왼쪽부터 i-2까지 길이가 덮개로 이미 채워져 있으면 1x2 덮개 2개 혹은 2x2 덮개 하나를
넣는 경우로 2가지 경우가 존재한다.
N-2 미만의 길이에 대해선 고려할 필요 없다. 사용할 수 있는 덮개의 형태가 최대 2x2 직사각형
형태이기 때문이다. 다시 말해 바닥을 채울 수 있는 형태는 위에서 언급한 경우밖에 없다.
따라서 다음과 같이 점화식을 세울 수 있다.

a i = a i-1 + a i-2 x 2

왼쪽부터 N-2까지 길이가 덮개로 채워져 있는 경우 덮개를 채우는 방법은 2가지 경우가 있다.
이 두 방법은 서로 다른 것이므로 결과적으로 a i는 a i-1 + a i-2 + a i-2가 된다.
따라서 간략하게 위의 식으로 표현할 수 있다.
"""