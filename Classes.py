class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age




class Dog(Animal):

    def __init__(self, kind):
        super.__init__()
        self.kind = kind

    # bark function - returns woof!
    def check_kind(self):
        print(f"Breed: {self.kind}, woof!")


dog1 = Dog("Seila", 8, 'golden retriever')
dog2 = Dog("Viggo", 4, 'husky')

dog1.check_kind()