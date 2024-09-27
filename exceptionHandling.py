arr = [1,2,3]
try:
    print(arr[1])
    print(arr[0]/5)
    if arr[2] > 5:
        temp = "hay"
    print(temp)
except (IndexError,ZeroDivisionError,NameError):
    print("Some error has occurred")
# except IndexError:
#     print("You are trying to access an element which doesn't exist!")
# except ZeroDivisionError:
#     print("You are trying to divide value by 0")
# except NameError:
#     print("Variable doesn't exist")
