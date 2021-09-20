# Multiplies two integers
def multiply(a: int,b: int) -> int:
    return a*b

# Divides two integers - 'b' must NOT be equal 0
def divide(a: int,b: int) -> int:
    if b == 0:
        print("can't divide by zero!")
    else:
        return a/b

# Subtracts two integers
def subtract(a: int,b: int) -> int:
    return a-b


# Adds two integers
def add(a: int,b: int) -> int:
    return a+b

print(multiply(3,4))
print(subtract(3,4))
print(divide(3,4))
print(divide(3,0))
print(add(3,4))