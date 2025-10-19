# 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def __add__(self, other):
            if self.author == other.author:
                return self.pages + other.pages
            else:
                return "Нельзя сложить книги разных авторов"


book1 = Book("Война и мир", "Лев Толстой", 1225)
book2 = Book("Анна Каренина", "Лев Толстой", 864)
book3 = Book("Преступление и наказание", "Фёдор Достоевский", 671)

print(book1)
print(book2)
print(book3)

print(book1 + book2)
print(book1 + book3)
# 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)


person1 = Person("Alice", 25)
print(person1.info)
print(Person.is_adult(20))
print(Person.is_adult(15))

person2 = Person.from_birth_year("Bob", 2000)
print(person2.info)