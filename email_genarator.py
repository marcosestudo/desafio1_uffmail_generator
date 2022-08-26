""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""

from csv import reader

registration_number = input("Insira o número da matrícula:\n")

class Aluno:
    """
    Class docstring
    """

    def __init__(self, nome, matricula, telefone, email, uffmail, status):
        self.__nome = nome
        self.__matricula = matricula
        self.__telefone = telefone
        self.__email = email
        self.__uffmail = uffmail
        self.__status = status


def csv_reader(file):
    with open(file, encoding='utf_8') as arq:
        leitor_csv = reader(arq, delimiter=',')

        # each iteration of for reads a row as an array
        for row in leitor_csv:
            if registration_number == row[1]:
                print(f"Nome: {row[0]}")
                break

csv_reader("alunos.csv")
