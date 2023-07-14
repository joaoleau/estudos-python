from cls import (
    Person,
    Product,
    PersonValidation,
    ProductService
)
from association import (
    Pen,
    Bag,
    Student,
    Student2,
    PenClass,
    StudentClass,
    StudentClass2,
    Objects,
)

"""Association"""
pen1 = Pen(
    mark="Bic",
    color="White"
)

student1 = Student(
    name="Joao",
    materials=[pen1]
)

bag1 = Bag(
    mark="Nike",
    color="Blue",
    size="large"
)

# print(PenClass(pen1).color)
PenClass(pen1).color = "Black"
# print(PenClass(pen1).color)

# print(StudentClass(student1).materials)
StudentClass(student1).add_material(bag1)
# print(StudentClass(student1).materials)


student2 = Student2(
    name="Igor",
    objects=[]
)

# print(StudentClass2(student2).student)
print(Objects(student2.objects).objects)
Objects(student2.objects).add_object(pen1)
print(Objects(student2.objects).objects)
print(StudentClass2(student2).objects)
print(StudentClass2(student2).student)
StudentClass2(student2).objects = bag1
print(StudentClass2(student2).objects)


"""Persons"""
# person1 = Person(
#     name="Joao",
#     email="joao@gmail.com",
#     age=18,
# )

# person2 = Person(
#     name="Joao",
#     email="joao@gmail.com",
#     year=2005
# )

# PersonValidation().create(person1)
# person2 = PersonValidation.create_year(person2)
# print(person1.age)
# print(person2.age)

"""Products"""
# product1 = Product(
#     name="Mouse",
#     price=200
# )

# product2 = Product(
#     name="Headset",
#     price=400
# )

# print(ProductService(product1).discount(10))

# print(ProductService(product2).price)
# print(ProductService(product2).discount(20))
# print(ProductService(product2).price)
# ProductService(product2).price = 1000
# print(ProductService(product2).price)
