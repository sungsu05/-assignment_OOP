from abc import abstractmethod

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f"{self.name}은 {self.age}에요 멍멍")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}은 {self.age}에요 야옹")

test1 = Dog("초코",5)
test2 = Cat("애옹",3)

test1.speak()
test2.speak()