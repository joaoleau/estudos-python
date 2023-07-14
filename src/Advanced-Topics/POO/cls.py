from dataclasses import dataclass
import re
import datetime

#########################################################################################

"""Exceptions"""

class InvalidEmail(Exception):
    """Exception"""

class InvalidName(Exception):
    """Exception"""

class InvalidAge(Exception):
    """Exception"""

class InvalidPrice(Exception):
    """Exception"""

########################################################################################

"""Class Person"""

@dataclass
class Person:
    name: str
    email: str
    age: int = None
    year: int = None


class PersonValidation:
    def __email__(self, email: str) -> str|InvalidEmail:
        pattern = re.compile("[\w]+@[\w]+\.com[\.\w]*")
        if re.fullmatch(pattern, email) is not None:
            return email

        raise InvalidEmail(print("InvalidEmail"))

    def __name__(self, name: str) -> str|InvalidName:
        pattern = re.compile("[a-zA-Z]+")
        if re.fullmatch(pattern, name) is not None:
            return name

        raise InvalidName(print("InvalidName"))

    def __age__(self, age: int) -> int|InvalidAge:
        if age >= 18:
            return age

        raise InvalidAge(print("InvalidAge"))

    @classmethod
    def create_year(cls, person: Person) -> Person:
        year = datetime.datetime.today().year
        age = year - person.year
        
        new_person = cls().create(Person(
            name=person.name,
            email=person.email,
            age=age
        ))
        
        return new_person

    def create(self, person: Person) -> Person:
        self.__email__(person.email)
        self.__name__(person.name)
        self.__age__(person.age)
        return person

###########################################################################################

"""Class Product"""

@dataclass
class Product:
    name: str
    price: float

class ProductService:
    def __init__(self, product: Product) -> None:
        self._product = product

    def discount(self, discount):
        self._product.price -= (self._product.price*(discount/100))
        return self._product.price

    @property
    def price(self):
        return self._product.price
    
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            raise InvalidPrice(print("InvalidPrice"))
        
        self._product.price = value
    
#############################################################################################