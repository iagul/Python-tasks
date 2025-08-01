# FileName = "names.txt" 

# with open(FileName, "a") as file:
#     while True:
#         FirstName = input("Enter your first name: ")
#         if FirstName.lower() == "stop":
#             break

#         LastName = input("Enter your last name: ")
#         FullName = f"{FirstName} {LastName}\n"

#         file.write(FullName)
#         print("Name saved!\n")



# from nameparser import HumanName

# data = [
# "Evelyn Cook, 75, Nixonland",
#     "Dr. Briana Davidson, 22, South Hunterside",
#     "Karl Rios, 39, Olsonton",
#     "Bradley Carr, 68, Ortizburgh",
#     "Mr. Brian Hall DDS, 62, North Carol",
#     "Michael Russell, 78, South Tracyfurt",
#     "Laura Brooks MD, 88, Jessicahaven",
#     "Matthew Gordon, 18, Dennistown",
#     "Alex Adams, 22, East Heatherview",
#     "Randy Robertson, 79, West Joanna",
#     "Barry Moreno, 86, Joneschester",
#     "Destiny Black, 22, Gutierrezland",
#     "James Mckinney, 24, East Danielle",
#     "Todd Taylor, 30, South Stacyborough",
#     "Justin Quinn, 75, West Kevin",
#     "Teresa Waters, 75, Blairchester",
#     "Zachary Burton, 41, Martinezfort",
#     "Jennifer Mann, 53, Jaredmouth",
#     "Kristen Johnson, 36, Port Kyle",
#     "John Stanley, 32, Smithville",
#     "Travis Baker, 49, Millerland",
#     "Haley Dunn, 24, Port Rachel",
#     "Margaret Franklin, 25, Jamieborough",
#     "Desiree Villegas, 38, South Danielton",
#     "Aaron Jones, 88, Port Amandamouth",
#     "Vanessa Smith, 25, Lake Elizabethmouth",
#     "Brittany Woods, 22, Lake Charles",
#     "Allen Ballard, 60, West Lauren",
#     "Lorraine Mcmahon, 32, West Brian",
#     "Nicholas Martinez, 76, North Charlene",
#     "Frank Conley, 87, Port Alec",
#     "Pamela Moses, 33, Livingstonmouth",
#     "Renee Johnson, 57, New Benjaminchester",
#     "Kevin Taylor, 60, Kellyville",
#     "Christopher Newman, 59, Christinachester",
#     "Michelle Harris, 86, Lake Ryan",
#     "Haley Carson, 69, New Tara",
#     "Sophia Vang, 61, Charlesbury",
#     "Billy Carey, 82, New Kurtchester",
#     "Sharon Ward, 49, Port Jean",
#     "Daniel Williams, 46, New Peter",
#     "Brian Beasley, 76, Zacharymouth",
#     "Michelle Middleton, 56, South Jasonmouth",
#     "Kelly Stout, 59, Tuckerside",
#     "Kathryn Schultz, 28, Gardnermouth",
#     "Shannon Johnston, 40, Kimland",
#     "John Bowen, 71, Sotofort",
#     "Nicole Moore, 56, Lake Justin",
#     "Janice Villarreal, 76, South Andrea",
#     "Jennifer Haney DVM, 24, Bassstad",
#     "Robert Tanner, 23, East Meredith",
#     "Julie Ramos, 73, Jeffreyfort",
#     "Jennifer Gray, 47, New Jonburgh",
#     "Derek Solomon, 36, Shawnton",
#     "Jennifer Price, 40, Michaelberg",
#     "Elizabeth Terrell, 90, South Joshua",
#     "John Roberts, 87, South Nicole",
#     "Michael Garcia, 71, Port Loriville",
#     "Dustin Moran, 68, Loganview",
#     "Laura Burns, 24, East Tammy",
#     "Lisa Neal, 20, New Craig",
#     "Natalie Hubbard, 70, Alexandraburgh",
#     "Bobby Wilkins, 24, Fergusonport",
#     "Meredith Miller DDS, 31, Johnsstad",
#     "Tyler Hernandez, 78, Jamesberg",
#     "Carrie Fletcher, 63, North Sarah",
#     "Michael Harris, 81, Jonathantown",
#     "Patrick David, 44, Gillfort",
#     "John Mccoy, 82, Hannahville",
#     "Robert Burch, 61, Lake Thomasmouth",
#     "Diane Davis, 54, Morrishaven",
#     "Herbert Mckinney, 88, Lake Debrastad",
#     "Andrew Hendricks, 22, Goodhaven",
#     "Krista Jackson, 79, Alexandrahaven",
#     "Tiffany Morgan, 76, Anneberg",
#     "Lee Maldonado, 64, Port Heidi",
#     "Wesley Carter, 58, Annafort",
#     "John Cannon, 22, Norrisville",
#     "Mariah Weber, 41, Port Danielmouth",
#     "Tanner Carr, 79, Bradleyside",
#     "Donald Irwin, 77, Port Jennifer",
#     "Sherry Garza, 60, North Tonyaland",
#     "Michael Madden, 45, West Christina",
#     "Stacy Moore, 38, Crystaltown",
#     "Charles Davenport, 87, Emilybury",
#     "Jamie Andrade, 84, Jasonchester",
#     "Christine Hicks, 73, Ryanside",
#     "Sarah Tyler, 89, Tammyberg",
#     "Becky Quinn MD, 25, Jesseport",
#     "James Banks, 87, Bryantburgh",
#     "Kathleen Sandoval, 51, New Bradleyfort",
#     "Victor Johnson, 51, North Mariebury",
#     "Jennifer Lopez, 83, Melissafort",
#     "Sarah Lambert, 52, Patrickborough",
#     "Kathryn Grant, 50, Matthewport",
#     "Jacqueline Vaughan, 55, South John",
#     "Andrea Williams, 54, New Glenn",
#     "Curtis Smith, 70, Tateville",
#     "Edward Miller, 55, Atkinsfort",
#     "Haley Orozco, 72, Port Carlosfurt"
# ]

# with open("Less50.txt", "w") as less50_file, open("Over50.txt", "w") as over50_file:
#     for entry in data:
#         name_part, age_part, city_part = entry.rsplit(', ', 2)
#         age = int(age_part.strip())
#         city = city_part.strip()
        
#         name = HumanName(name_part.strip())

#         output = f"{name.first} {name.last}, {age}, {city}\n"

#         if age < 50:
#             less50_file.write(output)
#         else:
#             over50_file.write(output)

# print("Processing complete. Check Less50.txt and Over50.txt.")
