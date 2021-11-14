class Dog:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        

    def meow(self):
        return "meow"

    def add_one(self, x):
        return x + 1


    def bark(self):
        print("bark")


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


    def set_age(self,age):
        self.age = age


d = Dog("john smith",12)
d2 = Dog("jane doe",20)
d.bark()
d.meow()

print(d.get_age())
d.set_age(21)
print(d.get_age())



print(d.add_one(5))
print(type(d))




#https://www.youtube.com/watch?v=JeznW_7DlB0