""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""
from student import Student


enrollment_number = input("Digite sua matrícula:\n")


student = Student.csv_reader("alunos.csv", enrollment_number)


# if enrollment number are not find, the student can´t be instantiated
if student:
    options = student.uffmail_generator()

    # if student have not active status or already have an uffmail, can't see the options of uffmail_generator
    if options:
        chosen_option = student.options_printer(options)
        student.uffmail_creator(options, chosen_option)
