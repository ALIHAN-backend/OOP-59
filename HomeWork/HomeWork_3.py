class Car:
    def __init__(self, brand):
        self.brand = brand                 # публичный атрибут
        self._fuel_level = 0               # защищённый атрибут
        self.__engine_status = False       # приватный атрибут

    def start_engine(self):
        if self._fuel_level > 0:
            self.__engine_status = True
            print("Двигатель запущен!")
        else:
            print("Невозможно завести двигатель — нет топлива!")

    def stop_engine(self):
        self.__engine_status = False
        print("Двигатель выключен.")

    def drive(self, distance):
        if self.__check_fuel(distance):
            fuel_needed = distance * 0.1
            self._fuel_level -= fuel_needed
            print(f"Проехали {distance} км, осталось {self._fuel_level:} литров топлива.")
        else:
            print("Недостаточно топлива для поездки!")

    def refuel(self, amount):
        self._fuel_level += amount
        print(f"Заправлено {amount} литров топлива. Текущий уровень: {self._fuel_level:} л.")

    def get_status(self):
        engine_state = "включен" if self.__engine_status else "выключен"
        return f"Марка: {self.brand} | Топливо: {self._fuel_level:} | Двигатель: {engine_state}"

    def __check_fuel(self, distance):
        return self._fuel_level >= distance * 0.1


# Пример использования:
car = Car("Toyota")
car.refuel(10)
car.start_engine()
car.drive(50)
print(car.get_status())