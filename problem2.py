from abc import abstractstaticmethod, abstractproperty, ABC


class PokemonTrainIntrface(ABC):

    @abstractstaticmethod
    def increase_experience(self, value):
        pass

    @abstractproperty
    @abstractstaticmethod
    def experience(self):
        pass


class Pokemon(PokemonTrainIntrface):
    def __init__(self, name, category) -> None:
        self.category = category
        self.name = name
        self._experience = 100

    @property
    def experience(self):
        return self._experience

    def increase_experience(self, value: int):
        self.experience = self.experience + value

    @experience.setter
    def experience(self, value):
        self._experience = value


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', category='grass')
    bulbasaur.increase_experience(100)
    print(bulbasaur.experience)
