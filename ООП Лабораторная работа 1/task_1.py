# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Any
import doctest

class Player:
    def __init__(self, name: str, health: int):
        """
        Создание и подготовка к работе объекта "Игрок"

        param name: имя игрока
        param health: здоровье игрока

        Пример:
        >>> player_1 = Player("Artem", 5000)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not 0 <= len(name) <= 50:
            raise ValueError("Имя должно быть не длиннее 50 символов")
        self.name = name

        if not isinstance(health, int):
            raise TypeError("Здоровье должно быть типа int")
        if health < 0:
            raise ValueError("Здоровье игрока не может быть меньше нуля")
        self.health = health

    def heal_player(self, cure: int) -> int:
        """
        Функция исцеления игрока

        :param cure: значение, на которое исцеляется игрок
        :raise ValueError: Если новое значение здоровья превышает максимальное, то возвращается ошибка

        :return: здоровье игрока
        Пример:
        >>> player_2 = Player("Алиса", 3500)
        >>> player_2.heal_player(500)
        """
        ...

    def upgrade_armor(self, armor) -> int:
        """
        Функция улучшения брони

        :param armor: значение, на которое увеличивается общее здоровье игрока (броня)

        :return: новое значение здоровья (здоровье+броня)

        Пример:
        >>> player_3 = Player("Михаил", 5500)
        >>> player_3.upgrade_armor(500)
        """
        ...


class Weapon:
    def __init__(self, force: int, capacity: int, bullet_count: int):
        """
        Создание и подготовка к работе объекта "Оружие"

        param force: наносимый урон
        param capacity: емкость магазина
        param bullet_count: количество пуль в магазине

        Примеры:
        >>> AK_74 = Weapon(250, 30, 30)
        >>> Makarov = Weapon(150, 8, 7)
        >>> RPG_7 = Weapon(2000, 1, 1)
        """

        if not isinstance(force, int):
            raise TypeError("Наносимый урон должен быть типа int")
        if not force > 0:
            raise ValueError("Наносимый урон должен быть положительным числом")
        self.force = force

        if not isinstance(capacity, int):
            raise TypeError("Емкость магазина должна быть типа int")
        if capacity <= 0:
            raise ValueError("Емкость магазина дожна быть положительным числом")
        self.capacity = capacity

        if not isinstance(bullet_count, int):
            raise TypeError("Количество пуль в магазине должно быть типа int")
        if bullet_count < 0:
            raise ValueError("Количество пуль должно быть не меньше нуля")
        if bullet_count > capacity:
            raise ValueError("Количество пуль не может превышать емкость магазина")
        self.bullet_count = bullet_count

    def shoot(self):
        """
        Функция стрельбы из оружия
        """
        ...
    def reload(self):
        """
        Функция перезарядки
        """
        ...
    def upgrade(self, improvment: int) -> int:
        """
        Функция улучшения оружия
        :param improvment: значение единиц, на которое увеличивается сила оружия

        :retutn: новое значение силы оружия

        Пример:
        >>> SVD = Weapon(2500,5, 5)
        >>> SVD.upgrade(300)
        """
        ...

class Enemy:

    def __init__(self, health: int, enemy_damage: int):
        """
        Создание и подготовка к работе объекта "Противник"

        param health: здоровье
        param damage: наносимый врагом урон

        Примеры:
        >>> enemy_level_1 = Enemy(1000, 50)
        >>> enemy_level_34 = Enemy(7500, 500)
        """
        if not isinstance(health, int):
            raise TypeError("Здоровье должно быть типа int")
        if health < 0:
            raise ValueError("Здоровье не должно быть меньше нуля")
        self.health = health

        if not isinstance(enemy_damage, int):
            raise TypeError("Наносимый врагом урон должен быть типа int")
        if enemy_damage <= 0:
            raise ValueError("Наносимый врагом урон должен быть больше нуля")
        self.enemy_damage = enemy_damage

    def hurt(self, damage: int, hitting: bool):
        """
        Функция ранения врага
        """
        hitting_ = hitting
        if hitting_ is True:
            self.health -= damage
        if self.health <=0:
            return print("Враг уничтожен")
        else:
            return print("Здоровье врага: ", self.health)

    def intoxication(self, poison):
        """
        Функция отравления врага

        :param poison: значение, на которое будет снижаться здоровье врага каждые 5 секунд, на протяжении 30 секунд

        :return: новое значение здоровья врага

        Пример:
        >>> enemy_level_34 = Enemy(7500, 500)
        >>> enemy_level_34.intoxication(50)
        """

        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod() # Тестирование примеров из документации