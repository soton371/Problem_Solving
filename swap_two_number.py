def swap(num1: int, num2: int):
    num1 = num1 ^ num2
    num2 = num2 ^ num1
    num1 = num1 ^ num2

    print(f'num1: {num1}, num2: {num2}')
