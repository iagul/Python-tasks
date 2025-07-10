# import csv

# def collect_and_write_data(num_entries):
#     filename = "users_data.csv"
#     fieldnames = ["ID", "first_name", "last_name", "age"]
    
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
        
#         for i in range(1, num_entries + 1):
#             first_name = input(f"{i}. Enter first name: ")
#             last_name = input(f"{i}. Enter last name: ")
            
#             while True:
#                 try:
#                     age = int(input(f"{i}. Enter age: "))
#                     break
#                 except ValueError:
#                     print("Invalid input! Please enter an integer for age.")
            
#             writer.writerow({"ID": i, "first_name": first_name, "last_name": last_name, "age": age})
    
#     print(f"Data successfully written to {filename}")

# num_entries = int(input("How many entries do you want to add? "))
# collect_and_write_data(num_entries)

