def find_single_number():
    numbers = [1, 2, 1, 4, 2]
    result = 0
    for number in numbers:
        result = result ^ number
    print(f"result: {result}")

