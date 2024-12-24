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

# ฟังก์ชันสำหรับคำนวณ Postfix Expression
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}
    
    # แยกคำจากนิพจน์และทำการคำนวณ
    for token in expression.split():
        if token not in operators:
            # ถ้าเป็นตัวเลข ให้ผลักลง Stack
            stack.push(float(token))
        else:
            # ถ้าเป็นตัวดำเนินการ ให้ดึงตัวเลขจาก Stack และคำนวณ
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 != 0:
                    result = operand1 / operand2
                else:
                    return "Error: Division by zero"
            
            # ผลลัพธ์นำผลักกลับไปยัง Stack
            stack.push(result)
    
    # เมื่อคำนวณเสร็จ ผลลัพธ์สุดท้ายจะอยู่ใน Stack
    return stack.pop()

# รับนิพจน์จากผู้ใช้งาน
postfix_expression = input("กรุณากรอก Postfix Expression (เช่น 3 4 + 2 *): ")

# คำนวณและแสดงผลลัพธ์
result = evaluate_postfix(postfix_expression)
print("ผลลัพธ์ของ Postfix Expression:", result)
