x = int(input("ความกว้าง = "))
y = int(input("ความยาว = "))

print("พื้นที่", x * y)
i = 1
import math

while True:
    print("\n===== โปรแกรมคำนวณพื้นที่และเส้นรอบรูป =====")
    print("1. สี่เหลี่ยมผืนผ้า")
    print("2. สามเหลี่ยม")
    print("3. วงกลม")
    print("4. ออกจากโปรแกรม")

    choice = input("เลือกเมนู (1-4): ")

    if choice == "1":
        x = float(input("ความกว้าง = "))
        y = float(input("ความยาว = "))

        area = x * y
        perimeter = 2 * (x + y)

        print("พื้นที่ =", area)
        print("เส้นรอบรูป =", perimeter)

    elif choice == "2":
        base = float(input("ฐาน = "))
        height = float(input("ความสูง = "))

        area = 0.5 * base * height

        print("พื้นที่สามเหลี่ยม =", area)

    elif choice == "3":
        radius = float(input("รัศมี = "))

        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius

        print("พื้นที่วงกลม =", round(area, 2))
        print("เส้นรอบวง =", round(circumference, 2))

    elif choice == "4":
        print("ขอบคุณที่ใช้โปรแกรม")
        break

    else:
        print("กรุณาเลือกเมนู 1-4")
