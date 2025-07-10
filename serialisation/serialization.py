import json
import os

def add_persons(count, filename='persons.json'):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            persons = json.load(f)
    else:
        persons = []

    max_id = max(p['id'] for p in persons) if persons else 0

    for _ in range(count):
        name = input("enter your name: ")
        try:
            age = int(input("enter your age: "))
        except:
            age = 0
            print("age gotta be a number, setting to 0")

        max_id += 1
        persons.append({"id": max_id, "name": name, "age": age})

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(persons, f, ensure_ascii=False, indent=4)

    print(f"added {count} new peeps to {filename}")

if __name__ == "__main__":
    try:
        n = int(input("how many peeps you wanna add? "))
    except:
        n = 1
    add_persons(n)
