import sys
N = int(sys.stdin.readline())

dic = [0] * 1000001
dic[1] = 1
dic[2] = 2
dic[3] = 3
dic[4] = 5
dic[5] = 8

for i in range(3, N+1):
    dic[i] = (dic[i-2] + dic[i-1]) % 15746
print(dic[i])
