def plus():
    pass


class User:
    def __init__(self, name, phone=""):
        self.name = name
        self.phone = phone
        self.__params = {}

    def __eq__(self, other):
        if isinstance(other, User):
            ok = self.name == other.name
            self.name += "!"
            return ok

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def __getattr__(self, item):
        if self.__params.get(item):
            return self.__params.get(item)
        return ""



class PhoneBook:
    def __init__(self, name=""):
        self.name=name
        self.list = []

    def add(self, user):
        self.list.append(user)
        return True

    def search(self):
        name = input("Кого ищем")
        user_temp = User(name)

        for u in self.list:
            if u == user_temp:
                return u
        return None

    def delete(self, user):
        pass

    def __str__(self):
        return f"Телефонная книга {len(self.list)} записей"

class Engine:
    def on(self):
        pass
    def speedup(self):
        pass
    def speeddown(self):
        pass

class EngineDiesel(Engine):
    def __init__(self, ls=100, rpmmax=1000):
        self.ls = ls
        self.status = False
        self.rpm = 0
        self.__rpmmax = rpmmax

    def on(self):
        self.status = True
        print("Поднимаем обороты")
        self.rpm = 200


    def speedup(self):
        print("Ускоряемся")
        if self.rpm < self.__rpmmax:
            self.rpm += 100

    def speeddown(self):
        if not self.status:
            return
        print("Тормозим")
        if self.rpm > 0:
            self.rpm -= 100
        if self.rpm < 0:
            self.rpm = 0
            self.status = False

    def __str__(self):
        return f"Двигатель {self.status}, скорость {self.rpm}"

class EngieBenzin(Engine):
    __rpm: int
    __rpmmax: int

    def __init__(self, ls:int=100,) -> object:
        self.ls = ls
        self.status = False
        self.__rpm = 0
        self.__rpmmax = ls*10

    def get_current_rpm(self) -> int:
        return self.__rpm

    def get_max_rpm(self) -> int:
        return self.__rpmmax

    def on(self):
        if self.status:
            return
        else:
            print("Поднимаем обороты")
            self.__rpm = 200
            self.status = True

    def speedup(self):
        if not self.status:
            return

        if self.__rpm < self.__rpmmax:
            self.__rpm += 100

    def speeddown(self):
        if not self.status:
            return
        print("Тормозим")
        if self.__rpm > 0:
            self.__rpm -= 100
        if self.__rpm < 0:
            self.__rpm = 0
            self.status = False

    def __str__(self):
        return f"Двигатель {self.status}, скорость {self.get_current_rpm()} из {self.get_max_rpm()}"

class Car:
    def __init__(self,name, engine:Engine):
        self.name = name
        self.engine = engine
        self.stops = False

    def poehali(self):
        self.stops = False
        self.engine.on()

    def speedup(self):
        self.stops = False
        self.engine.speedup()

    def speeddown(self):
        self.stops = True
        self.engine.speeddown()

    def __str__(self):
        return f"Я машина {self.name} двигатель: {self.engine} {'СТОП' if self.stops else '-'}"

def poehali(mycar):
    mycar.poehali()

if __name__ == "__main__":
    e1: EngieBenzin = EngieBenzin(1200)
    print(e1.get_max_rpm())
    car = Car("Красная красивая", e1)
    print(car)
    car.poehali()
    print(car)
