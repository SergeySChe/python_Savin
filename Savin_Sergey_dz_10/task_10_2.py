from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.cloth / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.cloth) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)
