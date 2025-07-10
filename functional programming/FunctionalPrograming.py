# Numbers = [(1, 3), (4, 2), (2, 5)]

# SortedNumbers = sorted(Numbers, key=lambda x: x[1])

# print(SortedNumbers)

# def DivideNUmbers(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("dont divide by 0")
#     except TypeError:
#         print('type in numbers')
#     else:
#         print(f"result {result}")
    

# DivideNUmbers(10,3) 

# DivideNUmbers(10, 0)

# DivideNUmbers("10", 'a') 

# DivideNUmbers(13, 3)

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]    

# def filter(products):
#     for i in products:
#         if i["price"] < 100:
#             print(i)

# filter(products)

# def map(products):
#     for i in products:
#         print(i["name"], i["price"])
        
# map(products)

# def get_price(product):
#     return product["price"] 

# products.sort(key=get_price)

# sorted_products = [(p["name"], p["price"]) for p in products]

# print(sorted_products)

# from functools import reduce

# def add(x,y):
#     return x + y

# products_price = [i['price'] for i in products]

# print(products_price)

# res = reduce(add, products_price)

# print(res)