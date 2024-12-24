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

# ฟังก์ชันเพื่อกลับลำดับตัวอักษรในข้อความ
def reverse_string(text):
    stack = Stack()

    # เก็บแต่ละตัวอักษรใน Stack
    for char in text:
        stack.push(char)

    reversed_text = ""
    # ดึงตัวอักษรจาก Stack ออกมาและรวมเป็นข้อความที่กลับลำดับ
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text

# รับข้อความจากผู้ใช้งาน
input_text = input("กรุณากรอกข้อความที่ต้องการกลับลำดับ: ")

# แสดงผลลัพธ์
reversed_text = reverse_string(input_text)
print("ข้อความที่กลับลำดับแล้ว:", reversed_text)
