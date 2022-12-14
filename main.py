""" uffmail generator.
Reads a .csv file with students informations, searchs for a student by enrollment number,
returns a list of uffmail options based on the student's name to be chosen, create the ufmail and
send the password to the estudent phone.
"""
from student import Student


def main():
    CSV_FILE = "alunos.csv"
    enrollment_number = input("Digite sua matrícula:\n")

    student = Student.csv_reader(CSV_FILE, enrollment_number)

    # if enrollment number are not find, the student can´t be instantiated, the program is finished
    if student:
        options = student.uffmail_options_generator(CSV_FILE)

        # if student have not active status or already have an uffmail, can't see the options of uffmail_generator, the program is finished
        if options:
            chosen_option = student.options_printer(options)
            student.uffmail_creator(chosen_option, CSV_FILE)
            student.password_sender()


if __name__ == "__main__":
    main()
