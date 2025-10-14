# class Test:
#      # Магический метод
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#        return self.name
#
# class MyInt:
#     def __init__(self, value):
#          self.value = value
#
#     def __str__(self):
#        return self.value
#
# test3 = MyInt(123)
# test4 = 123
#
# print(test4)

# class Money:
#
#     def __init__(self, amount, currency):
#         self.amount = amount
#         self.currency = currency
#
#     #                +
#     def __add__(self, other):
#         if self.currency == other.currency:
#             print(self.amount + other.amount)
#         else:
#             print(f'Currency error')
#         print(self.currency)
#         print(other.currency)
#         print(self.amount + other.amount)
#     #                <
#     def __lt__(self, other):
#         print(self.amount)
#         print(other.amount)
#     #                >
#     def __gt__(self, other):
#         print(self.amount)
#         print(other.amount)
#
# SOM = Money(100, 'SOM')
#
# USD = Money(100, 'USD')
#
# new_obj = SOM > USD

# class MyList:
#
#     def __init__(self, value: list):
#         self.value = value
#
#   def __new__(cls, *args, **kwargs):
#
#   def __setitem__(self, key, value):
#         print(key) = [1]
#         print(value) = 123
#
#   def __getitem__(self, item):
#         print(item)
#
#   def __del__(self):
#
# test2 = MyList([1,23,4,56,7])
# test2[1] =  123

# class Test:
#     #  Атрибута класса
#     name = "Class Name"
#     def __init__(self, value):
#     # Атрибута экземпляра класса
#      self.value = value
#
#   def test(self):
#        pass
#
#   def __test2(self):
#       pass
#
#     def _just_method(self):
#         print(f"{self.value} я все")
#
#     @staticmethod
#     def static_method():
#         print("я все")
#
#     @classmethod
#     def class_method(cls):
#         print(cls.name)
#
#     @property
#     def property_method(self):
#         return "Atrebut"
#
# objects = Test("test")
# Test.static_method()
# Test._just_method()
# print(objects.value)
# print(objects._just_method())
# print(objects.property_method)

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

john = User('John', 'Doe')
print(john.get_full_name)