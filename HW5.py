class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# ฟังก์ชันตรวจสอบลำดับความสำคัญของตัวดำเนินการ
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# ฟังก์ชันแปลง Infix เป็น Postfix
def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    for char in expression:
        if char.isdigit():  # ถ้าเป็นตัวเลขให้เพิ่มไปยังผลลัพธ์
            postfix.append(char)
        elif char == '(':  # ถ้าเป็นวงเล็บเปิดให้ผลักลงใน Stack
            stack.push(char)
        elif char == ')':  # ถ้าเป็นวงเล็บปิดให้ดึงตัวดำเนินการจาก Stack
            while stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # ลบวงเล็บเปิดออกจาก Stack
        else:  # ถ้าเป็นตัวดำเนินการ
            while (not stack.is_empty() and precedence(stack.peek()) >= precedence(char)):
                postfix.append(stack.pop())
            stack.push(char)

    # ดึงตัวดำเนินการที่เหลือออกจาก Stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

# ฟังก์ชันคำนวณผลลัพธ์จาก Postfix Expression
def evaluate_postfix(postfix):
    stack = Stack()
    for char in postfix:
        if char.isdigit():  # ถ้าเป็นตัวเลขให้ผลักลงใน Stack
            stack.push(int(char))
        else:  # ถ้าเป็นตัวดำเนินการให้ดึงตัวเลขจาก Stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2)

    return stack.pop()

# ฟังก์ชันประเมินผล Infix Expression
def evaluate_infix(expression):
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result

# รับ Infix Expression จากผู้ใช้
infix_expression = input("กรุณากรอก Infix Expression (เช่น 3 + 5 * (2 - 8)): ")

# คำนวณผลลัพธ์ของ Infix Expression
result = evaluate_infix(infix_expression)
print(f"ผลลัพธ์ของ Infix Expression '{infix_expression}' คือ: {result}")
