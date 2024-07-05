def stack():
    s = []
    return s
def push(s, data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s):
    return s[len(s) - 1]
def isEmpty(s):
    return s == []
def size(s):
    return len(s)

def isPostfix(postfix):
    operand = stack()                                 
    print("Operand Stack:", operand)
    for i in range(len(postfix)):
        if postfix[i] in "0123456789":
            push(operand, i)
        elif postfix[i] in "+-/*":
            if size(operand) < 2: 
                return False 
            else:      
                operand2 = pop(operand)
                operand1 = pop(operand)
                push(operand, operand1 + operand2 + i)
        else: 
            return False
    if size(operand) > 1: 
        return False

    return True 

def evaluatePostfix(postfix):
    if not isPostfix(postfix):
        print("POSTFIX YANG ANDA MASUKAN TIDAK VALID!!!!")
        return False

    operandStack = stack()
    operator = '+-/*'
    for i in postfix:
        if i not in operator: 
            push(operandStack, i)
        else:             
            oprnd2 = pop(operandStack)
            oprnd1 = pop(operandStack)
            if i == '+':
                result = int(oprnd1) + int(oprnd2)
            elif i == '-':
                result = int(oprnd1) - int(oprnd2)
            elif i == '*':
                result = int(oprnd1) * int(oprnd2)
            else:
                result = int(oprnd1) / int(oprnd2)
            push(operandStack, result)
        print("Operand Stack:", operandStack)
    return pop(operandStack)


evaluatePostfix("1+2")
evaluatePostfix("12+")