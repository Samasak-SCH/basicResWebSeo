while True:
    brand = input("Car's brand : ")
    if len(brand) <= 20:
        break
    print("Not more than 20 characters")

while True:
    model = input("Car's model : ")
    if len(model) <= 20:
        break
    print("Not more than 20 characters")

while True:
    try:
        year = int(input("Year of product : "))
        if len(str(year)) == 4:
            break
        print("Not more than 4 characters")
    except ValueError:
        print("Number only!!!")

while True:
    color = input("Car's color : ")
    if len(color) <= 10:
        break
    print("Not more than 10 characters")

while True:
    try:
        price = float(input("Car's prices : "))
        break
    except ValueError:
        print("Number or Decimal!!!")

print(f"\nCar information : ")
print(f"1. Brand    : {brand}")
print(f"2. Model    : {model}")
print(f"3. Year     : {year}")
print(f"4. Color    : {color}")
print(f"5. Price    : {price:.2f}")