from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class cat(Animal):
    def speak(self):
        print("mio mio")

class dog(Animal):
    def speak(self):
        print("Bho Bho")

obj = cat()
obj.speak()
# print(dir(obj))
# obj.speak()
