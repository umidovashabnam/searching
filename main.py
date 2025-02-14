# class Person:
#     def __init__(self,name,fam):
#         self.name = name
#         self.fam = fam
#     def say_hi(self):
#         print("salom")
#
# class Student(Person):
#     def say_hi(self):
#         print(f"Assalomu aleykum, mening ismim{self.name}")
#
#
# class Pupil(Person):
#     pass
# s = Student("shabnam","umidova")
#
# p = Pupil("munisa","sultonmurodova")
# p.say_hi()


#
# class Transport:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
#
#     def info(self):
#         pass
#
#
#
# class Car (Transport):
#     pass
#
# t = Transport("bus","100")
# c = Car("bmw","200")
# print(c.brand)
# print(c.speed)



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot, {self.name}, Narx, {self.price}, {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor ")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount


class Food(Product):
    def __init__(self, name, price, quantity, muddati):
        super().__init__(name, price, quantity)
        self.muddati = muddati

    def info(self):
        data = super().info()
        data += f" || muddati, :{self.muddati}"
        return data



class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f" {self.warranty}"
        return data


e = Electronics("phone", 1000, 12, "1 yil", )
print(e.info())