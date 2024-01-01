class Color():
    """Этот класс хранит цвет
    Aттрибутами класса служит яркость трех каналов
    Cогласно кодировке RGB
    """

    def __init__(self, r: int, g: int, b: int) -> None:
        """Инициализация цвета согласно кодировке RGB
        Яркость кажого канала в пределах [0,255]
        Args:
            R (int): Яркость красного канала
            G (int): Яркость зеленого канала
            B (int): Яркость синего канала
        """
        if not all([0 <= luminance <= 255 for luminance in (r, g, b)]):
            raise ValueError('Яркость каналов дожна быть в пределах [0,255]')
        self.rgb = r, g, b

    def __repr__(self) -> str:
        """Выводит цвет обьекта

        Returns:
            str: строчное представление класса
        """
        end = '\033[0'
        start = '\033[1;38;2'
        mod = 'm'
        red_level, green_level, blue_level = self.rgb
        rep = f'{start};{red_level};{green_level};{blue_level}{mod}●{end}{mod}'
        return rep

    def __eq__(self, other) -> bool:
        """Функция для сравнения цветов

        Args:
            other (Color): цвет для сравнения

        Returns:
            bool: Равенсто цветов
        """
        if not isinstance(other, type(self)):
            raise TypeError('Можно сравнивать только цвета!')

        colors = list(zip(self.rgb, other.rgb))
        for color1, color2 in colors:
            if color1 != color2:
                return False

        return True

    def __add__(self, other):
        """Смешивание цветов поканально

        Args:
            other (Color): цвет для добавления

        Returns:
            Color: результатирующий цвет
        """
        if not isinstance(other, type(self)):
            raise TypeError('Можно смешивать только цвета!')

        colors = list(zip(self.rgb, other.rgb))
        return Color(*[sum(color) for color in colors])

    def __hash__(self) -> int:
        """уникальный хеш для обьекта

        Returns:
            int: знацение хеша
        """
        r, g, b = self.rgb
        return r * 10**6 + g * 10**3 + b

    def __mul__(self, c: float):
        """Снижение контраста

        Args:
            c (float): контраст [0,1]

        Returns:
            Color: Цвет после изменения контраста
        """
        if not 0 <= c <= 1:
            raise ValueError('Контраст должен быть в [0,1]')

        cl = -256 * (1 - c)
        f = 259 * (cl + 255) / 255 / (259-cl)

        return Color(
                    *[128 + round(f * (luma - 128))
                      for luma in self.rgb]
                )

    def __rmul__(self, c):
        """Снижение контраста

        Args:
            c (float): контраст [0,1]

        Returns:
            Color: Цвет после изменения контраста
        """
        return self * c


if __name__ == '__main__':
    # Task1
    print(10*'=', ' Task 1 ', 10*'=')
    red = Color(255, 0, 0)
    print(red)

    # Task2
    print(10*'=', ' Task 2 ', 10*'=')
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)

    # Task2
    print(red == Color(255, 0, 0))

    # Task3
    print(10*'=', ' Task 3 ', 10*'=')
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)

    # Task 4
    print(10*'=', ' Task 4 ', 10*'=')
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    # Task 5
    print(10*'=', ' Task 5 ', 10*'=')
    print((0.5 * red))
