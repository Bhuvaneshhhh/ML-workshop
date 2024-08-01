def divide(a, b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b
try:
    result=divide(10, 0)
except ValueError as e:
    print(e)
