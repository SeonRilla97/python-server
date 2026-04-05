
while True:

    input_str = input("계산식을 입력하세요: ")
    
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    
    if input_str == "+":
        print(add(num1, num2))
    elif input_str == "-":
        print(sub(num1, num2))
    elif input_str == "*":
        print(mul(num1, num2))
    elif input_str == "/":
        print(div(num1, num2))
    elif input_str == "exit":
        print("계산기를 종료합니다.")
        break
    else:
        print("잘못된 연산자입니다.")
    

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
