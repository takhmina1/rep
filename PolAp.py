# 'abstaksiy-abs-'

# """
# Создайте абстрактный класс Animal с абстрактным методом sound().
# Создайте подклассы Dog и Cat,
# которые наследуются от Animal и реализуют метод sound(),
# который выводит соответствующий звук для каждого животного.

# """


# # from abc import ABC,abstractmethod
# # # from math import *

# # class Animal(ABC):
    
# #     @abstractmethod
# #     def sound():
# #         return f'ndfk'
    


# # class Dog(Animal):
# #     def sound():
# #          return 'Gav-gav'

    


# # class Cat(Animal):
# #     def sound():
# #         return 'Miy-miy'



# # print(Animal.sound())
# # print(Cat.sound())
# # print(Dog.sound())


# """
# 2. Создайте абстрактный класс Shape с абстрактным методом area().
# Создайте подклассы Rectangle и Circle,
# которые наследуются от Shape и реализуют метод area(), 
# который вычисляет площадь прямоугольника и круга соответственно.

# """

# # class Shape(ABC):
    
# #     def area():
# #         return 'res'
        
        
    
# # class Rectangle(Shape):
    
# #     def area():
# #         return a * b
        

# # class Circle(Shape):
    
# #     def area():
# #         pass
    

# """
# Создайте класс "Фрукт" с методом "представить_себя()". 
# Создайте дочерние классы "Яблоко", 
# "Апельсин" и "Банан", 
# которые переопределяют метод "представить_себя()" и выводят информацию о себе.
# Создайте массив объектов класса "Фрукт" и вызовите метод "представить_себя()" для каждого объекта.
    
    
# """
    
# class Frut():

#     def frit():
#         return 'выводят информацию Фрукт'
    
# class Apple(Frut):
    
#     def frit():
#         return 'apple'
        
# class Apelsin(Frut):
    
#     def frit():
#         return 'yellow'

# class Banane(Frut):
    
#     def frit():
#         return 'banane'
    

# """
# Создайте абстрактный класс Animal с абстрактным методом sound().
# Создайте подклассы Dog и Cat,
# которые наследуются от Animal и реализуют метод sound(),
# который выводит соответствующий звук для каждого животного.

# """


# # from abc import ABC,abstractmethod
# # # from math import *

# # class Animal(ABC):
    
# #     @abstractmethod
# #     def sound():
    
# a = Apelsin
# print(Frut.frit())
# print(a.frit())
# print(Apple.frit())
# print(Banane.frit())





# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# rectangle = Rectangle(5, 4)
# circle = Circle(3)

# print("Площадь прямоугольника:", rectangle.area())
# print("Площадь круга:", circle.area())


# class Fruit:
#     def eat(self):
#         print("Фрукт съеден")

# class Apple(Fruit):
#     def eat(self):
#         print("Яблоко съедено")

# apple = Apple()

# apple.eat()




