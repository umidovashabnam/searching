class Product:

# Obyektlar yaratish
phone = Electronics("iPhone 15", 1200, 10, 2)
laptop = Electronics("MacBook Pro", 2500, 5, 3)
apple = Food("Olma", 3, 100, "2025-06-15")

# Ma'lumotlarni chiqarish
print(phone.info())
print(laptop.sell(2))
print(apple.restock(20))