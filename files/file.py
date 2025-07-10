file_name = "names.txt"


with open(file_name, "a") as file:
    count = 1  
   
    with open(file_name, "r") as f:
        lines = f.readlines()
        if lines:
            count = len(lines) + 1  

    while True:
        first_name = input("Enter your first name: ")
        if first_name.lower() == "stop":
            break 

        last_name = input("Enter your last name: ")

        file.write(f"{count}. {first_name} {last_name}\n")
        count += 1
