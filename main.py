""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""
from student import Student


enrollment_number = input("Insira o número da matrícula:\n")


aluno = Student.csv_reader("alunos.csv", enrollment_number)
print(aluno.get_name())
