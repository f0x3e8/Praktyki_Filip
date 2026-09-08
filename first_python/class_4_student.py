class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_passed(self):
        if self.average() >= 3:
            return True
        else:
            return False

    def passing_students(students):
        passing_students = []
        for i in students:
            if i.has_passed():
                passing_students.append(i)
        return passing_students

    def student_names(students):
        student_names = []
        for i in students:
            student_names.append(i.name)
        return student_names

    def best_student(students):
        best_average = students[0].average()
        best_name = students[0].name
        for i in students:
            if i.average() > best_average:
                best_average = i.average()
                best_name = i.name
        return best_name

students = [
    Student("Adam", [5, 4, 3]),
    Student("Bartek", [2, 2, 3]),
    Student("Kasia", [5, 5, 4]),
    Student("Ola", [3, 2, 2]),
]

print(Student.student_names(Student.passing_students(students)))
# ["Adam", "Kasia"]

print(Student.best_student(students))
# Kasia