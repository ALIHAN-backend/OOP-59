class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def action(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}")


person1 = Person("Алиса", 19, "Москва")
person2 = Person("Боб", 18, "Санкт-Петербург")

# Вызов метода
person1.action()
person2.action()
