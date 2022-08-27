""" file containing uffmail generator student class """
from csv import reader


class Student:
    """ Class of student containing name, enrollment, telephone, email, uffmail (if any)
    and subscription status (active or inactive);
    method for reading .csv file with student information and
    uffmail generation method based on student name
    """
    def __init__(self, student):
        self.__name = student[0]
        self.__enrollment_number = student[1]
        self.__phone = student[2]
        self.__email = student[3]
        self.__uffmail = student[4]
        self.__status = student[5]


    @staticmethod
    def csv_reader(file, enrollment_number):
        """ instantiates a student with the information read from a .csv file passed as an argument
        """
        with open(file, encoding='utf_8') as arq:
            leitor_csv = reader(arq, delimiter=',')

            # each iteration of for reads a row as an array
            for row in leitor_csv:
                if enrollment_number == row[1]:
                    return Student(row)

        return 'Matrícula não encontrada.'


    def uffmail_generator(self):
        """ Generate uffmail options array to be chosen based on the user full name """
        uffmail_options = []

        full_name_array = self.get_name().lower().split(" ")

        uffmail_options.append("".join(name for name in full_name_array) + ('@id.uff.br'))
        uffmail_options.append(full_name_array[0] + full_name_array[1] + '@id.uff.br')
        uffmail_options.append(full_name_array[0] + full_name_array[-1] + '@id.uff.br')
        uffmail_options.append(full_name_array[0] + "_" + full_name_array[1] + '@id.uff.br')
        uffmail_options.append(full_name_array[0] + "_" + full_name_array[-1] + '@id.uff.br')

        for i in range(len(full_name_array)):
            for j in range(len(full_name_array)):
                # deep copy auxiliary variable
                aux = list(full_name_array)
                if i==j:
                    aux[i] = full_name_array[i][0]
                    uffmail_options.append("".join(name for name in aux) + ('@id.uff.br'))
                    if i < len(full_name_array) - 1:
                        aux[i + 1] = full_name_array[i + 1][0]
                        uffmail_options.append("".join(name for name in aux) + ('@id.uff.br'))

        return uffmail_options


    def options_printer(self, options):
        """ Show the uffmail options in the screen and return the chosen number """
        print(f'\n{self.__name.split(" ")[0]}, por favor escolha uma das opções abaixo para o seu UFFMail')

        for index, generated_string in enumerate(options):
            print(f'{index + 1} - {generated_string}')

        print()

        chosen_option = int(input()) - 1

        valid_options = []

        for i in range(len(options)):
            valid_options.append(i)

        while chosen_option not in valid_options:
            print('\nEscolha uma opção válida')

            for index, generated_string in enumerate(options):
                print(f'{index + 1} - {generated_string}')
            
            print()

            chosen_option = int(input()) - 1

        return chosen_option


    def uffmail_creator(self, options, chosen_option):
        """ Creates the chosen uffmail and sends the password to the user phone number """
        print(f'A criação de seu e-mail ({options[chosen_option]}) será feita nos próximos minutos.')

        return options[chosen_option]


    def get_name(self):
        """ returns student name """
        return self.__name


    def get_enrollment(self):
        """ returns student enrollment number """
        return self.__enrollment_number


    def get_phone(self):
        """ returns student phone number """
        return self.__phone


    def get_email(self):
        """ returns student email """
        return self.__email


    def get_uffmail(self):
        """ returns student uffmail """
        return self.__uffmail


    def get_status(self):
        """ returns student subscription status """
        return self.__status
