def canSeePersonsCount(heights):
    res = []
    for i in range(len(heights)):
        stack = []
        c = 0
        for j in range(i+1,len(heights)):
            if heights[i] <= heights[j]:
                c += 1
                break
            else:
                if len(stack) == 0:
                    stack.append(heights[j])
                    c += 1
                else:
                    if heights[j] > stack[len(stack) - 1]:
                        stack.append(heights[j])
                        c += 1
        res.append(c)
    print(res)

canSeePersonsCount([10,6,8,5,11,9])
