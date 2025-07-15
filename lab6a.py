#!/usr/bin/env python3
# Author ID: SMEEP-KAUR

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # ensure number is stored as a string
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if not self.courses:
            return 'GPA of student ' + self.name + ' is 0.0'
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]


if __name__ == '__main__':
    # Create first student and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student and add grades
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Output student1 info
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Output student2 info
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
