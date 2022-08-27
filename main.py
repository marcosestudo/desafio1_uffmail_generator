""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""
from student import Student


enrollment_number = input("Digite sua matrícula:\n")


student = Student.csv_reader("alunos.csv", enrollment_number)


if student == 'Matrícula não encontrado.':
    print('Matrícula não encontrada.')
else:
    options = student.uffmail_generator()
    chosen_option = student.options_printer(options)
    student.uffmail_creator(options, chosen_option)