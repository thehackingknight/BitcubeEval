# AUTHOR: THABISO KOZA
class Person:

    def __init__(self, forenames, emali_address, surname, date_of_birth):
    
        self.forenames = forenames
        self.emali_address = emali_address
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.first_name = forenames[0]
        self.full_name = " ".join(forenames) + " " + surname

class Student(Person):

    def __init__(self, forenames, emali_address, surname, date_of_birth, link_to_degree):
        super().__init__(forenames, emali_address, surname, date_of_birth)
        self.link_to_degree = link_to_degree


class Lecture:

    def __init__(self, forenames, emali_address, surname, date_of_birth, degrees):
        super().__init__(forenames, emali_address, surname, date_of_birth)
        self.degrees = degrees

class DC:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class Degree(DC):

    def __init__(self, name, duration, courses, lecturer):
        super().__init__(name, duration)
        self.courses = courses
        self.lecturer = lecturer

class Course(DC):

    def __init__(self, name, duration, courses, degree):
        super().__init__(name, duration)
        self.courses = courses
        self.degree = degree


