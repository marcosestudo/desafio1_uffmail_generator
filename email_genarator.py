from csv import reader

registration_number = input("Insira o número da matrícula:\n")

with open("alunos.csv", encoding='utf_8') as arq:
    leitor_csv = reader(arq, delimiter=',')

    for row in leitor_csv:
        if registration_number == row[1]:
            print(f"Nome: {row[0]}")
            break
