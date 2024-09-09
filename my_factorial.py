def myFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * myFactorial(n -1)