# the program calculates sum of numbers between two zeros in the array

def find_sum(arr):
    res = []
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            i += 1
        else:
            j = i + 1
            status = False
            while j < len(arr):
                if arr[j] == 0:
                    status = True
                    break
                else:
                    j += 1
            if status:
                sum_ = sum(arr[i:j])
                res.append(sum_)
            i = j
    print(res)

find_sum([1,0,2,3,0,3,0,4,5,0,4])
