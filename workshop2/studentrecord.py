#from uc_student import *

import uc_student as u

from workshop2.uc_student import Student, demographics

if __name__ == '__main__':
    student1 = u.demographics()
    std1 = Student(student1[0],student1[1],student1[2])

    student2 = u.demographics()
    std2 = Student(student2[0],student2[1],student2[2])

    student3 = u.demographics()
    std3 = Student(student3[0], student3[1], student3[2])

    print(f'Student1 student number: {std1.student_number()} ')
    print(f'Student1 student number: {std2.student_number()} ')
    print(f'Student1 student number: {std3.student_number()} ')

    print(f'Student1 student ID: {std1.student_id()} ')
    print(f'Student1 student ID: {std2.student_id()} ')
    print(f'Student1 student ID: {std3.student_id()} ')

    print(f'Total number of students: {Student.student_count}')


