#q1
#a
data = {}

n = int(input("Enter dict length: "))
for i in range(n):
    key = int(input("Enter key: "))
    val = input("Enter value: ")
    data[key] = val

data_tup = tuple(data.items())
print(data)
print(data_tup)

#b
data_length = {}
keys = list(data.values())
print(keys)
for i in keys:
    data_length[i] = len(i)

print(data_length)

#c
temp_key = int(input("enter key: "))
temp_val = input("enter val: ")
temp_data = (temp_key,temp_val)
if temp_data in data.items():
    print("available")
else:
    print('NA')

#q2
menu = {
    "Biriyani":{
        "Price":520,
        "Rating":4.32
    },
    "Fried Rice":{
        "Price":110,
        "Rating":4.17
    },
    "Tea":{
        "Price":10,
        "Rating":4.89
    }
}

#a
def items_above_500():
    max_price = 500
    max_price_item = None
    items = list(menu.keys())
    for i in items:
        if menu[i]['Price'] > max_price:
            max_price_item = i
            max_price = menu[i]['Price']

    print(max_price_item)

#b
def highest_rated_item():
    max_rating = 0
    max_price_item = None
    items = list(menu.keys())
    for i in items:
        if menu[i]['Rating'] > max_rating:
            max_price_item = i
            max_rating = menu[i]['Rating']

    print(max_price_item)
