import json
from typing import Any
from keyword import iskeyword


class DictToObject:
    """Базовый класс который создает из json аттрибуты"""
    def __init__(self, dictionary: dict):
        """Вскрывает json"""
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """переопределен что бы keyword не мог быть аттрибутом"""
        if iskeyword(__name):
            __name = __name + "_"
        self.__dict__[__name] = __value


class ColorizeMixin():
    """Миксин добавляет цвета"""
    def __str__(self) -> str:
        """отвечает за строковое определение класса + цвета"""
        name = self.title
        price = self.price
        color = self.repr_color_code
        return f'\033[0;{color};{name}|{price} $\n'


class Advert(ColorizeMixin, DictToObject):
    """Классовое тображение обьявлений, имеет свой цвет"""
    repr_color_code = 32

    def __init__(self, data: dict):
        """Инициализирует обьявление из json или dict
           Так же проверяет на присутсвие title
           И положительное значение price
        """
        super().__init__(data)
        # то что ниже не в базовом классе,
        # а тут что показалось мне более уместным
        if 'price' not in self.__dict__:
            setattr(self, 'price', 0)
        if self.price < 0:
            raise ValueError('Price can not be negative')
        if 'title' not in self.__dict__:
            raise KeyError('No title attribute')


if __name__ == '__main__':

    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
    "address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print('_' * 30)

    dog_str = """{
    "title": "Вельш-корги", "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    print(dog_ad.class_)
    print('_' * 30)

    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    print(iphone_ad)
