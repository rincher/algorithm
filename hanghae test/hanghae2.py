import sys
# 큐 관련해서는 deque를 사용하는게 좋은것 같다
from collections import deque

# 입력 받을 카드의 갯수만큼
N = int(sys.stdin.readline())

# 카드를 입력할 양뱡향 큐를 선언하고
stack = deque()
# 선언한 데크에 받은 카드로 채우고
for i in range(1, N+1):
    stack.append(i)


def last_card(N):
    # 데크에 카드가 한장 남을 때 까지 돌리고
    while len(stack) > 1:
        # 위에서 한장
        stack.popleft()
        # 밑으로 한장
        stack.append(stack.popleft())
    # 정마담에게 남은 한장
    return stack.pop()


# 동작그만 밑장 빼기냐
print(last_card(N))
