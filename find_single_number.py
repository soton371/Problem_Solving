def find_single_number():
    numbers = [6, 3, 6, 7, 3]
    result = 0
    for number in numbers:
        result = result ^ number
    print(f"result: {result}")
