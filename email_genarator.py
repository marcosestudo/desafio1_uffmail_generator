""" uffmail generator.
Reads a .csv file with students informations, searches for a student by enrollment number
and returns a list of uffmail options based on the student's name.
"""

from csv import reader

enrollment_number = input("Insira o número da matrícula:\n")

class Student:
    """ Class of student containing name, enrollment, telephone, email, uffmail (if any)
    and subscription status (active or inactive);
    method for reading .csv file with student information and
    uffmail generation method based on student name
    """
    def __init__(self, name, enrollment, phone, email, uffmail, status):
        self.__name = name
        self.__enrollment = enrollment
        self.__phone = phone
        self.__email = email
        self.__uffmail = uffmail
        self.__status = status


    @staticmethod
    def csv_reader(file):
        with open(file, encoding='utf_8') as arq:
            leitor_csv = reader(arq, delimiter=',')

            # each iteration of for reads a row as an array
            for row in leitor_csv:
                if enrollment_number == row[1]:
                    print(f"Nome: {row[0]}")
                    break


    def get_name(self):
        """ returns student name """
        return self.__name


    def get_enrollment(self):
        """ returns student enrollment number """
        return self.__enrollment


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


Student.csv_reader("alunos.csv")
