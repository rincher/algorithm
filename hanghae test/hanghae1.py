import sys
# n = int(sys.stdin.readline())
# card_1 = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# card_2 = list(map(int, sys.stdin.readline().split()))


n = 5
card_1 = [6, 3, 2, 10, -10]
m = 8
card_2 = [10, 9, -5, 2, 3, 4, 5, -10]
result = True


for i in range(m):
    low = 0
    end = n
    while low <= end:
        middle = (low + end) // 2
        if card_2[i] in card_1[:middle]:
            print(1)
            break
        else:
            low = middle + 1
    print(0)

print(card_2[:2])
