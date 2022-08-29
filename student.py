""" file containing uffmail generator student class """
from csv import reader, writer
from unicodedata import normalize

class Student:
    """ Class of student containing name, enrollment, telephone, email, uffmail (if any)
    and subscription status (active or inactive);
    method for reading .csv file with student information;
    uffmail generator method based on student name;
    options printer method to show uffmail options list;
    uffmail creator method to create the chosen uffmail option and
    method to send sms message with the new uffmail password to the student phone.
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
            csv_reader = reader(arq, delimiter=',')

            # each iteration of for reads a row as an array
            for row in csv_reader:
                # testing if return error for trying to read an empty line and ignore then
                try:
                    if enrollment_number == row[1]:
                        # if finds the enrollment, instantiates a student
                        return Student(row)
                except IndexError:
                    pass

        print('\nMatrícula não encontrada.')

        return 0


    def uffmail_options_generator(self):
        """ Checks if the user have an active status and no uffmail. Then, generate an uffmail
        options array to be chosen based on the user full name
        """
        if self.__status == 'Inativo':
            print('\nVocê não possui matrícula ativa.')
            return 0

        if self.__uffmail:
            print('\nVocê já possui um uffmail.')
            return 0

        uffmail_options = []

        # removing accents and uppercased letters from name before generate the uffmails options list
        normalized_full_name = normalize('NFKD', self.get_name()).encode('ASCII','ignore').decode('ASCII').lower()
        # creating an array to generate the options
        full_name_array = normalized_full_name.split(" ")

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
                    # creating an option with one abbreviated name and pushing to the options array
                    aux[i] = full_name_array[i][0]
                    uffmail_options.append("".join(name for name in aux) + ('@id.uff.br'))
                    if i < len(full_name_array) - 1:
                        # creating an option with two abbreviated name and pushing to the options array
                        aux[i + 1] = full_name_array[i + 1][0]
                        uffmail_options.append("".join(name for name in aux) + ('@id.uff.br'))

        return uffmail_options


    def options_printer(self, options):
        """ Shows the uffmail options in the screen and return the chosen one """
        print(f'\n{self.__name.split(" ")[0]}, por favor escolha uma das opções abaixo para o seu UFFMail')

        for index, uffmail_option in enumerate(options):
            print(f'{index + 1} - {uffmail_option}')

        print()

        chosen_option = input()

        #  testing if the user are trying to pass a non numeric digit as an imput
        try:
            chosen_option = int(chosen_option) - 1
        except ValueError:
            chosen_option = -1

        valid_options = []

        # creating an array with valid number options based on name length
        for i in range(len(options)):
            valid_options.append(i)

        while chosen_option not in valid_options:
            print('\nEscolha uma opção válida')

            for index, uffmail_option in enumerate(options):
                print(f'{index + 1} - {uffmail_option}')

            print()

            chosen_option = input()

            try:
                chosen_option = int(chosen_option) - 1
            except ValueError:
                chosen_option = -1

        return options[chosen_option]


    def uffmail_creator(self, chosen_option, file):
        """ Creates the chosen uffmail and updates the .csv file """
        print(f'\nA criação de seu e-mail ({chosen_option}) será feita nos próximos minutos.')

        # auxiliary array to create the updated .csv file
        new_file_array = []

        # opening the document in read mode to fill the array with the updated document information
        with open(file, 'r', encoding='utf_8') as arq:
            csv_reader = reader(arq, delimiter=',')

            # filling the array with the updated document's rows
            for row in csv_reader:
                # testing if return error for trying to read an empty line and ignore then
                try:
                    if self.__enrollment_number == row[1]:
                        row[4] = chosen_option
                        self.__uffmail = row[4]
                        new_file_array.append(row)
                    else:
                        new_file_array.append(row)
                except IndexError:
                    new_file_array.append(row)

        # openig in write mode for update
        with open(file, 'w', encoding='utf_8', newline='') as arq:
            csv_writer = writer(arq, delimiter=',')
            csv_writer.writerows(new_file_array)

        return self.__uffmail


    def password_sender(self):
        """ Sends a message containing the uffmail password to the student phone number """

        if self.__uffmail:
            print(f'Um SMS foi enviado para {self.__phone} com a sua senha de acesso.')
            return 'Success'

        print("Você ainda não possui um uffmail")
        return 'err - inexistent uffmail'


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
