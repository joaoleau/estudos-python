from dataclasses import dataclass, field


@dataclass
class Wheels:
    size: str
    color: str = field(default='Black')


@dataclass
class Car:
    brand: str
    price: float = field(compare=False)
    model: str
    color: str = field(compare=False)
    size: str = field(compare=False)
    _airbags: bool = field(default=False, repr=False, compare=False)
    _accesories: list[object] = field(
        default_factory=list, repr=False, compare=False)

    def add_accesories(self, obj: object):
        self._accesories.append(obj)

    @property
    def airbags(self):
        return self._airbags

    @airbags.setter
    def airbags(self, new: bool):
        self._airbags = new


w1 = Wheels('Medium')
c1 = Car('Volks', 12000, 'Gol', 'White', 'Large')
c2 = Car('Volks', 12000, 'Gol', 'Yellow', 'Large', [w1])
print(c1 == c2)
print(c2)
