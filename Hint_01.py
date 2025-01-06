while True:
    inputVar = input("กรุณาป้อนค่าที่ต้องการ : ")
    if len(inputVar) <= 10:
        break
    print("กรุณาป้อนค่าที่ต้องการไม่เกิน 10 ตัวอักษร")
print(f"\nค่าที่ต้องการคือ : {inputVar}")