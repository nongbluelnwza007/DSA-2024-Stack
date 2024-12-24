class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# ฟังก์ชันตรวจสอบความถูกต้องของ JSON string
def validate_json(json_string):
    stack = Stack()
    # คู่ของเครื่องหมายที่เปิดและปิด
    opening = {'{', '[', '"'}
    closing = {'}': '{', ']': '[', '"': '"'}
    
    for char in json_string:
        if char in opening:
            stack.push(char)
        elif char in closing:
            # ถ้าพบเครื่องหมายปิด แต่ไม่มีเครื่องหมายเปิดที่ตรงกันใน Stack
            if stack.is_empty() or stack.pop() != closing[char]:
                return False

    # ตรวจสอบว่า Stack ว่างหรือไม่หลังจากตรวจสอบหมดแล้ว
    return stack.is_empty()

# รับ JSON string จากผู้ใช้งาน
json_input = input("กรุณากรอก JSON string: ")

# ตรวจสอบความถูกต้อง
if validate_json(json_input):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
