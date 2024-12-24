class Stack:
    def __init__(self):
        # ใช้ list ในการเก็บข้อมูลของ Stack
        self.stack = []

    # ฟังก์ชันเพื่อเพิ่มข้อมูลเข้า Stack
    def push(self, item):
        self.stack.append(item)

    # ฟังก์ชันเพื่อดูข้อมูลบนสุดของ Stack โดยไม่ลบข้อมูล
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None  # ถ้า Stack ว่าง

    # ฟังก์ชันเพื่อเอาข้อมูลออกจาก Stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  # ถ้า Stack ว่าง

    # ฟังก์ชันเช็คว่า Stack ว่างหรือไม่
    def is_empty(self):
        return len(self.stack) == 0

    # ฟังก์ชันเพื่อแสดงข้อมูลใน Stack
    def show(self):
        return self.stack

# สร้าง Stack
my_stack = Stack()

# ทดสอบการ push ข้อมูล 5 ตัว
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)

# แสดงข้อมูลบนสุด
print("ข้อมูลบนสุดของ Stack:", my_stack.peek())  # ควรแสดง 50

# ทดสอบ pop ข้อมูลออก 3 ตัว
print("Pop ข้อมูลออก:", my_stack.pop())  # ควรแสดง 50
print("Pop ข้อมูลออก:", my_stack.pop())  # ควรแสดง 40
print("Pop ข้อมูลออก:", my_stack.pop())  # ควรแสดง 30

# แสดงข้อมูลที่เหลือใน Stack
print("ข้อมูลที่เหลือใน Stack:", my_stack.show())  # ควรแสดง [10, 20]
