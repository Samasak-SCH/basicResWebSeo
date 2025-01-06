name = input("Please insert your name : ")
while True:
    try:
        birth_year = int(input("Please insert year of your birth (2024 is current year): "))
        break
    except ValueError:
        print("Please fill in numbers only")


current_year = 2024
age = current_year - birth_year

print(f"Hello Khun {name} and you are {age} years old")