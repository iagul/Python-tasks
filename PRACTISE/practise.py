# from car import Car

# car1 = Car("Mercerdess", 2006, "White", False ) # type: ignore
# car2 = Car("Mustang", 2020, "Blue", True)
# car3 = Car("Charger", 2026, "Yellow", True)

# print(car1.Model)
# print(car1.Year)
# print(car1.Color)
# print(car1.ForSale)

# print(car2.Model)
# print(car2.Year)
# print(car2.Color)
# print(car2.ForSale)

# print(car3.Model)
# print(car3.Year)
# print(car3.Color)
# print(car3.ForSale)

# =======================================Faker==================================    

# import json, random
# from faker import Faker

# fake = Faker()

# print("name: ", fake.name())
# print("address: ", fake.address())
# print("email: ", fake.email())

# for _ in range(10):

#     print(fake.date_between(start_date = "-1y", end_date = "today"))

# for _ in range(10):
    # print(fake.name_male())
    # print(fake.name_female())

# from faker.providers import internet

# fake.add_provider(internet)
# print(fake.ipv4_private)

# =========================================JSON==============================================

# import json

# with open("data.json", "r") as f:
#     data = json.load(f)

# with open("data2.json", "w") as f:
#     json.dump(data, f)

     
# print(data.items())

# data = json.loads(json_string)  
# data['test'] = True

# new_json = json.dumps(data, indent = 2, sort_keys=True)
# print(new_json)
# print(data['students'][0])

# =================================multythreading=======================================================

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"u finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("u take out da trash")

def get_mail():
    time.sleep(4)
    print("u get da mail")

chore1 = threading.Thread(target=walk_dog, args=("scooby", "doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("everything is done")

# walk_dog()
# take_out_trash()
# get_mail()