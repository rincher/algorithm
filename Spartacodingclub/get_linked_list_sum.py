top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    ans = [0]*len(heights)
    while heights:
        height = heights.pop()
        for i in range(len(heights) - 1, 0, -1):
            if heights[i] > height:
                ans[len(heights)] = i + 1
                break
    return ans


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
