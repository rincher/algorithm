import sys

# 입력받을 수의 갯수
N = int(sys.stdin.readline())
# 받으 수를 넣을 리스트
array = []

for i in range(N):
    # 입력받은 수를
    numbers = int(sys.stdin.readline())
    # 받은 수를 리스트에 넣고
    array.append(numbers)

# array.sort() #이것때문에 백준에서 timeout이 걸렸다.

# 출력할때만 정력해서 출력 (array 자체의 변화는 없다.)
for i in sorted(array):
    print(i)
