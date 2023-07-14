from dataclasses import dataclass


@dataclass
class Bag:
    mark: str
    color: str
    size: str


class BagClass:
    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    @property
    def color(self):
        return self.__bag.color

    @color.setter
    def color(self, color):
        self.__bag.color = color


@dataclass
class Pen:
    mark: str
    color: str


class PenClass:
    def __init__(self, pen: Pen) -> None:
        self.__pen = pen

    @property
    def color(self):
        return self.__pen.color

    @color.setter
    def color(self, color):
        self.__pen.color = color


@dataclass
class Student:
    name: str
    materials: list[object]


class StudentClass:
    def __init__(self, student: Student) -> None:
        self.__student = student

    @property
    def name(self):
        return self.__student.name

    def add_material(self, material: object):
        self.__student.materials.append(material)

    @property
    def materials(self):
        return self.__student.materials


@dataclass
class Student2:
    name: str
    objects: list


class Objects:
    def __init__(self, list: list) -> None:
        self.objects = list

    def add_object(self, object: object):
        self.objects.append(object)

    def objects(self):
        return self.objects


class StudentClass2:
    def __init__(self, student: Student2) -> None:
        self.__student = student

    @property
    def objects(self):
        return self.__student.objects

    @objects.setter
    def objects(self, object):
        Objects(self.__student.objects).add_object(object)

    @property
    def student(self):
        return self.__student
