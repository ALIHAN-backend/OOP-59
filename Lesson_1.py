class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.h_name = name
        self.h_lvl =lvl
        self.h_hp = hp

    # Методы класса
    def action(self):
        return print(f"{self.h_name} base action!")

    def cast_spell(self):
        return print(f"Fire bool")

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 99, 11000)

# kirito.cast_spell() = Fire bool
# asuna.cast_spell() = Fire bool
# kirito.action() = Kirito base action!
# asuna.action() = Asuna base action!
# print(kirito.h_hp) = 1000
# print(asuna.h_hp) = 11000
# print(kirito.h_name) = Kirito

# integer = 123
# string = "Text"
# print(type(integer)) = <class 'int'>
# print(type(string)) = <class 'str'>