import json, random
from faker import Faker

fake = Faker()

def gen_students(n=100):
    lst = []
    for _ in range(n):
        lst.append({
            "first_name": fake.first_name(),
            "last_name":  fake.last_name(),
            "email":      fake.email(),
            "age":        random.randint(18, 70),
            "is_active":  random.choice([True, False])
        })
    return lst

students = gen_students()
with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

with open('students.json', 'r', encoding='utf-8') as f:
    all_studs = json.load(f)

active = [s for s in all_studs if s['is_active']]

with open('active_students.json', 'w', encoding='utf-8') as f:
    json.dump(active, f, ensure_ascii=False, indent=4)

print(len(students), 'students total')
print(len(active),   'students active')











