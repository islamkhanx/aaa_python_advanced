import json
from typing import Any
from keyword import iskeyword


class DictToObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if iskeyword(__name):
            __name = __name + "_"
        if __name == "price":
            if __value < 0:
                raise ValueError
        self.__dict__[__name] = __value


class ColorizeMixin():

    def __str__(self) -> str:
        name = self.title
        cena = self.price
        color = self.repr_color_code
        return f'\033[0;{color};{name}|{cena} $\n'


class Advert(ColorizeMixin, DictToObject):
    repr_color_code = 32

    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)
        if 'price' not in self.__dict__:
            setattr(self, 'price', 0)


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
