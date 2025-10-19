# Decorator:
# def simple_decorator(func):
#     def wrapper():
#         print("До")
#         func()
#         print("После")
#
# @simple_decorator
# def say_hello():
#     print("Hello")
#
# say_hello()

# def greeting_decorator(greeting):
#     def wrapper(name):
#         func(name)
#         print(f"{name} how are you?")
#         return wrapper
#
# @greeting_decorator
# def greeting(name):
#     print(f"{name} Hello! ")
#
# greeting("Alice")

# def greeting_decorator(func):
#     def wrapper(name):
#         func(name)
#         print(f"{name} как дела ?")
#     return wrapper
#
# @greeting_decorator
# def greeting(name):
#     print(f"{name} привет")
#
# greeting("Ardager")

# def class_decorator(cls):
#     class NewClass(cls):
#
#         def new_method(self):
#             return "I am new method!"
#     return NewClass
#
# @class_decorator
# class OldClass:
#     def old_method(self):
#         return "i am old class"
#
# obj1 = OldClass()
# print(obj1.old_method())
# print(obj1.new_method())

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
# ardager = User("Ardager", "admin")
#
# def is_admin(func):
#     def wrapper(user, command):
#         if user.role == "admin" and command == "ban":
#             func(user,command)
#         else:
#             print("Вы не админ или такой команды нет !!")
#     return wrapper
#
# @is_admin
# def ban(user, command):
#     print(f'{user.name} забанил пользователя!!')
#
# ban(ardager, "ban")

# Find Code:
# def find_element(array,target):
#     print(array[target])
#     for ind, num in enumerate(array):
#         if target == ind:
#             print("нашел")
#         else:
#             print("не нашел")
#
# find_element([1,33,543,54,2,343,4], 4)

def find_element(array, target):
    left, right = 0, len(array) -1

    while left <= right:
        mid = (left + right) // 2
        print(f"LEFT: {left} == RIGHT: {right}")
        print(mid)
        if array[mid] == target:
            return print("Found")
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print("Not Found")
    #
    # for i in array:
    #     if i == target:
    #         print("нашли")
    #     else:
    #         print("не нашли")

find_element([1,2,3,4,5,6,7,8,9,10,11], 11)
