N,  K = map(int, input().split())
cnt = 0
array = []
while N > 0:
    coin = int(input())
    array.append(coin)
    N -= 1
array.sort(reverse=True)

for i in array:
    if i <= K:
        cnt += K // i
        K %= i
print(cnt)
