class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def mid_rate(self):
        """ Средний балл студента """
        sum_rates = 0
        number_rates = 0
        for rates in self.grades.values():
            for rate in rates:
                sum_rates += rate
                number_rates += 1 
        if number_rates > 0:
            mid_rate_student = sum_rates / number_rates
            return mid_rate_student
        else:
            return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.mid_rate()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}"
            )
    
    def __gt__(self, other):
        """" Сравнение """
        if self.mid_rate() > other.mid_rate():
            return f'Средний балл у {self.name} {self.surname} больше чем у {other.name} {other.surname}'
        else:
            return f'Средний балл у {self.name} {self.surname} меньше чем у {other.name} {other.surname}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mid_rate(self):
        """ Средний балл лектора """
        sum_rates = 0
        number_rates = 0
        for rates in self.grades.values():
            for rate in rates:
                sum_rates += rate
                number_rates += 1 
        if number_rates > 0:
            mid_rate_lecturer = sum_rates / number_rates
            return mid_rate_lecturer
        else:
            return 0
    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.mid_rate()}"
    
    def __gt__(self, other):
        """ Сравнение """
        if self.mid_rate() > other.mid_rate():
            return f'Средний балл у {self.name} {self.surname} больше чем у {other.name} {other.surname}'
        else:
            return f'Средний балл у {self.name} {self.surname} меньше чем у {other.name} {other.surname}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


def mid_stud_rates(students, course):
    """ Подсчет среднего балла студентов по курсу """
    sum_rates = 0
    number_rates = 0
    for student in students:
        for rate in student.grades[course]:
            sum_rates += rate
            number_rates += 1
    if number_rates > 0:
        mid_rates = sum_rates / number_rates
        return mid_rates
    else:
        return f"оценки отсутвуют"


def mid_lect_rates(lecturers, course):
    """ Подсчет среднего балла лекторов по курсу"""
    sum_rates = 0
    number_rates = 0
    for lecturer in lecturers:
        for rate in lecturer.grades[course]:
            sum_rates += rate
            number_rates += 1
    if number_rates > 0:
        mid_rates = sum_rates / number_rates
        return mid_rates
    else:
        return f"оценки отсутвуют"
    

students = []
lecturers = []

best_student = Student('Rayan', 'Gosling', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
students.append(best_student)

best_student2 = Student('Gal', 'Gadot', 'women')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']
students.append(best_student2)

cool_mentor = Mentor('Morgan', 'Freeman')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Mentor('Robin','Williams')
cool_mentor2.courses_attached += ['Git']

cool_lecturer = Lecturer('Keanu', 'Reeves')
cool_lecturer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Python']
lecturers.append(cool_lecturer)

cool_lecturer2 = Lecturer('Harrison', 'Ford')
cool_lecturer2.courses_attached += ['Git']
cool_lecturer2.courses_attached += ['Python']
lecturers.append(cool_lecturer2)

cool_reviewer = Reviewer('Tom', 'Hanks')
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Al', 'Pacino')
cool_reviewer2.courses_attached += ['Git']
cool_reviewer2.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer2.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer2.rate_hw(best_student, 'Python', 6)

cool_reviewer.rate_hw(best_student2, 'Git', 10)
cool_reviewer2.rate_hw(best_student2, 'Git', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student2, 'Python', 7)

best_student.rate_hw(cool_lecturer, 'Git', 7)
best_student2.rate_hw(cool_lecturer, 'Git', 10)
best_student.rate_hw(cool_lecturer, 'Python', 6)
best_student2.rate_hw(cool_lecturer, 'Python', 8)

best_student.rate_hw(cool_lecturer2, 'Git', 9)
best_student2.rate_hw(cool_lecturer2, 'Git', 10)
best_student.rate_hw(cool_lecturer2, 'Python', 7)
best_student2.rate_hw(cool_lecturer2, 'Python', 9)

print(cool_reviewer)
print()
print(cool_lecturer2)
print()
print(best_student2)
print()
print(best_student > best_student2)
print(best_student2 > best_student)
print()
print(cool_lecturer > cool_lecturer2)
print(cool_lecturer2 > cool_lecturer)
print()
print(f"Средняя балл студентов по курсу Python - {mid_stud_rates(students, 'Python')}, Git - {mid_stud_rates(students, 'Git')}")
print()
print(f"Средняя балл лекторов по курсу Python - {mid_lect_rates(lecturers, 'Python')}, Git - {mid_lect_rates(lecturers, 'Git')}")