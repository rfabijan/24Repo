def addition(a=0,b=0):
    return a+b

def greeting(name: str, age: int) -> str:
    print(f'Hello {name}, Age {age}')

def multi_Args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)

def capture_first_name_from_cmd_line():
    pass

def multi_Args_add(*multiargs):
    total = 0
    for arg in multiargs:
        total += arg
    return total

print(multi_Args_add(1,5,5,6,7))