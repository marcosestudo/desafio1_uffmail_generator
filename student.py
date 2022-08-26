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
        self.__enrollment = student[1]
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

            return "Aluno não encontrado."


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
