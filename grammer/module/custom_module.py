'''
if __name__ == "__main__":
    print("이 코드는 직접 실행될 때만 작동합니다.")
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b
    
if __name__ == "__main__":
    print("이 코드는 직접 실행될 때만 작동합니다.")
    print(add(1, 2))
else:
    print("이 코드는 다른 모듈에서 import 되었습니다.")