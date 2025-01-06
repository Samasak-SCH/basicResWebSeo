while True:
    try:
        price = float(input("กรุณาใส่ราคาสินค้า : "))
        break
    except ValueError:
        print("กรุณาใส่ราคาเป็นตัวเลขหรือทศนิยม!!!")
print(f"\nราคาสินค้าคือ : {price}")