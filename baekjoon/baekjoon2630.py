import sys


def quad_tree(x, y, n):
    global array, blue, white
    color = array[y][x]
    double_break = False

    for i in range(x, x+n):
        if double_break:
            break

        for j in range(y, y+n):
            if array[j][i] != color:
                quad_tree(x, y, n//2)
                quad_tree(x + n//2, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                double_break = True
                break

    if not double_break:
        if array[y][x] == 1:
            blue += 1
        else:
            white += 1


# 변수 입력/선언
N = int(sys.stdin.readline())
array = []
blue = 0
white = 0

# 2차원 배열 입력받기
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

quad_tree(0, 0, N)
print(white)
print(blue)
