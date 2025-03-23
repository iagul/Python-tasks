# number = int(input("enter yo number"))
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial = factorial * i
#
# print(factorial)

# for i in range (1,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i*j}")

price  = 50
taxes = int(input("input tax:"))
if taxes != 5 and taxes != 10 and taxes !=20:
    print("araswori kupiura jigaro")
elif taxes == 5 or taxes == 10 or taxes == 20:
    print(f"gadasaxadi dagrcha {price - taxes}")
elif price != 50:
    print(f"kidev gadaixade {price - taxes}")

