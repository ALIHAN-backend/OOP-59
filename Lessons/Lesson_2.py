# # Наследование
#
# # Родительный класс|Супер класс
# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         return f'{self.name} base action'
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp: int = 10):
#         super().__init__(name,lvl,hp)
#         self.mp = mp
#
#     def cast_spells(self):
#         if self.mp == 0:
#             return "Не осталось маны"
#         self.mp -= 1
#         return f'{self.name} cast fire ball'
#
#     def action(self):
#         return f'{self.name} first step'
#
# class AssassinHero(Hero):
#
#     def action(self):
#         return f'{self.name} became invisible'
#
# kirito = Hero('Kirito', 2, 100)
# gendalf = MageHero('Gendalf', 1000, 1000000, 10)
# niga = AssassinHero('Niga', 100, 100)
# print(kirito.action())
# print(gendalf.cast_spells())
# print(niga.action())


class A:
    def action(self):
        return "A"

class B(A):
    def action(self):
        return super().action()

class C(A):
    def action(self):
        return "C"

class D(B,C):
    def action(self):
        return super().action()

obj_1 = D()
print(obj_1.action())
print(D.mro())