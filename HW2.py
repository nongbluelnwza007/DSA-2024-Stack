class Stack:
    def __init__(self):
        # ใช้ list ในการเก็บข้อมูลของ Stack
        self.stack = []

    # ฟังก์ชันเพื่อเพิ่มข้อมูลเข้า Stack
    def push(self, item):
        self.stack.append(item)

    # ฟังก์ชันเพื่อเอาข้อมูลออกจาก Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # ถ้า Stack ว่าง

    # ฟังก์ชันเช็คว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 2
def decimal_to_binary(n):
    stack = Stack()

    # ถ้า n เป็น 0 ให้ return "0"
    if n == 0:
        return "0"

    # แปลงเลขฐาน 10 เป็นฐาน 2 โดยใช้การหารและเก็บเศษใน Stack
    while n > 0:
        stack.push(n % 2)
        n = n // 2

    # ดึงข้อมูลจาก Stack เพื่อสร้างเลขฐาน 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())

    return binary

# ฟังก์ชันแปลงเลขฐาน 10 เป็นฐาน 16
def decimal_to_hexadecimal(n):
    stack = Stack()
    hex_digits = "0123456789ABCDEF"

    # ถ้า n เป็น 0 ให้ return "0"
    if n == 0:
        return "0"

    # แปลงเลขฐาน 10 เป็นฐาน 16 โดยใช้การหารและเก็บเศษใน Stack
    while n > 0:
        stack.push(hex_digits[n % 16])
        n = n // 16

    # ดึงข้อมูลจาก Stack เพื่อสร้างเลขฐาน 16
    hexadecimal = ""
    while not stack.is_empty():
        hexadecimal += str(stack.pop())

    return hexadecimal

# รับเลขฐาน 10 จากผู้ใช้งาน
decimal_number = int(input("กรุณากรอกเลขฐาน 10: "))

# แปลงเลขฐาน 10 เป็นฐาน 2 และฐาน 16
binary_result = decimal_to_binary(decimal_number)
hexadecimal_result = decimal_to_hexadecimal(decimal_number)

# แสดงผลลัพธ์
print(f"เลขฐาน 10 {decimal_number} แปลงเป็นฐาน 2: {binary_result}")
print(f"เลขฐาน 10 {decimal_number} แปลงเป็นฐาน 16: {hexadecimal_result}")
