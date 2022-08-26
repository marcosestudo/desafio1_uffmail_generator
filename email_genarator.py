""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""

from csv import reader

registration_number = input("Insira o número da matrícula:\n")

with open("alunos.csv", encoding='utf_8') as arq:
    leitor_csv = reader(arq, delimiter=',')

    # each iteration of for reads a row as an array
    for row in leitor_csv:
        if registration_number == row[1]:
            print(f"Nome: {row[0]}")
            break
