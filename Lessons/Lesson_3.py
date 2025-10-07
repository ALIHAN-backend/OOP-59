# Инкапсуляция

class BankAccount:

    def __init__(self, username, password, balance):
        self.username = username
        self._balance = balance # Защищенный атрибут  _
        self.__password = password # Приватный атрибут __

    def new_password(self, new_password):
        self.__password = new_password
        return 'Password changed successfully'

    def balance(self):
        return self._balance

    # def __get_random_password(self):
    #     return random.randint(1,10)
    #
    # def generate_password(self):
    #     return self.__get_random_password()


John = BankAccount("John", "12345", 100)

# print(John.new_password('<PASSWORD>'))
# print(John.balance())
# print(John._BankAccount__password)
# print(John.generate_password())

# Абстракция

from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#      def __init__(self, name):
#         self.name = name
#
#      def move(self):
#          return f"{self.name} step"
#
#      def make_sound(self):
#          return f"{self.name} Gaf Gaf"
#
# Gufi = Dog("Gufu")