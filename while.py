
while True:
    print("What's your Age:")
    age = input()
    if age.isdigit():
        age = int(age)
        if age<170:
            print("THANK YOU")
            break
        else:
            print("Are you a vampire?")


for digit in range(len(long_number)):
    product = 1
    for i in long_number[digit:digit+14]:
        if product > max_product:
            max_product = product
        i = int(i)
        product *= i
print(max_product)



