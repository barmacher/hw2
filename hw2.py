current_year = 2021
class Person:
    __total_persons = 0

    def __init__(self,name, birth_year, **kwargs):
        if birth_year > current_year:
            raise Exception("Error")
        else:
            self.__name = name
            self.__birth_year = birth_year
            self.__language = kwargs.get("language")
            self.increase()




    def get_language(self):
        return self.__language

    @classmethod
    def increase(cls):
        cls.__total_persons += 1
    @classmethod
    def get_total_persons(cls):
        return cls.__total_persons

    def is_adult(self):
        if current_year - self.__birth_year>=18:
            return True
        else:
            False

    def get_age(self):
        return current_year - self.__birth_year

    @classmethod
    def get_total_person(cls):
        return cls.__total_persons

    def talk(self):
        return "Hello World!"

class Teacher(Person):

    def talk(self):
        return "Greetings, I'm your teacher"
    def teach(self):
        return "Lesson started by Teacher"

p1 = Person("Igor", 2002, language="russian")
print(Person.get_total_persons())
p2 = Person("Kairat", 2001, language="kyrgyz")
print(Person.get_total_persons())
p3 = Person("Aidar", 1997, language="kazakh")
print(Person.get_total_persons())
p4 = Teacher("Karina", 2003, language="korean")
p5 = Teacher("Larisa", 1984)
p6 = Teacher("Vova", 1967)
print('Person p1', p1.get_language())
print('Person p2', p2.get_language())
print('Person p3', p3.is_adult())
print('Person p4', p4.is_adult(), p4.get_age())
print(p5.talk())
print(p4.teach())
print(Teacher.get_total_persons())


