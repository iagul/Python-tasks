# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33), 
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37),
#     ('Data', 'Guguchia', 17)
# ]

# while True:
#     FirstName = input("Enter name (or enter stop to stop the program): ")
#     if FirstName.lower() == "stop":
#         break

#     MatchingPersons = [p for p in persons if p[0] == FirstName]
#     if not MatchingPersons:
#         print("This name is not on the list.")
#         continue

#     LastName = input("Enter last/surname: ")
#     FullMatch = next((p for p in MatchingPersons if p[1] == LastName), None)

#     if FullMatch:
#         print(f"{FullMatch[0]} {FullMatch[1]} is {FullMatch[2]} years old.")
#     else:
#         print("This surname is not on the list.")

# print(set(input ("enter word 1")) & set(input ("enter word 2")))

print(set())