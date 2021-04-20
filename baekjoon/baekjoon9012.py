import sys

T = int(sys.stdin.readline())
array = []
for i in range(T):
    array = list(sys.stdin.readline().strip())
    left = array.count("(")
    right = array.count(")")
    if left != right:
        print("NO")
    else:
        print("YES")
