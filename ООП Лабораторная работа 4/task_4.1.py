class Computer:
    """
    Базовый класс "Компьютер"
    """
    def __init__(self, name: str = None):
        """
        Создание и подготовка к работе объекта "Компьютер"

        param name: производитель компьютера
        """
        if len(name) <= 0:
            raise ValueError("Имя производителя не может быть пустым значением")
        self.name = name


    def type(self) -> str:
        return "Компьютер"

    def __str__(self):
        return f'Производитель "{self.name}", Вид "{self.type()}"'

    def __repr__(self):
        return f'{self.__class__.__name__}, name={self.name!r}, type="{self.type()}"'

class Laptop(Computer):
    """
    Дочерний класс "Ноутбук"
    """
    def __init__(self, name, display: float = 15.6):
        super().__init__(name)

    def type(self) -> str:
        return "Ноутбук"

class Desktop(Computer):
    """
    Дочерний класс "Настольный компьютер"
    """
    def __init__(self, name):
        super().__init__(name)

    def type(self) -> str:
        return "Настольный компьютер"


if __name__ == "__main__":
    """
    Проверка методов __str__ и __repr__
    """
    comp1 = Computer("Apple")
    comp2 = Laptop("Acer")
    comp3 = Desktop("Apple")

    print(comp1)
    print(repr(comp1))
    print("")
    print(comp2)
    print(repr(comp2))
    print("")
    print(comp3)
    print(repr(comp3))


