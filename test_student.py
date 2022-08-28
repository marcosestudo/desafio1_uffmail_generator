from unittest import TestCase, mock, main
from csv import reader, writer
from student import Student


# To run tests
# >>> python -m unittest
# or
# >>> python -m unittest -v


def reset_file(file='alunos.csv'):
    """ reset the file alunos.csv to the original state before run the tests """
    original_state_file = 'alunos_original.csv'
    original_state_array = []

    with open(original_state_file, 'r', encoding='utf_8') as arq:
        csv_reader = reader(arq, delimiter=',')

        with open(original_state_file, 'r', encoding='utf_8', newline='') as original, open(file, 'w', encoding='utf_8', newline='') as file:
            csv_reader = reader(original, delimiter=',')
            csv_writer = writer(file, delimiter=',')

            for row in csv_reader:
                original_state_array.append(row)

            csv_writer.writerows(original_state_array)


class TestStudentMethods(TestCase):
    def test_student_name(self):
		# Tests if the student returned by the Student.csv_reader() method is correct by name
        reset_file()
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').get_name(), 'Luiza Fernandes Ferreira')

        self.assertEqual(Student.csv_reader('alunos.csv', '100503').get_name(), 'Vitor Fernandes Costa')

        self.assertEqual(Student.csv_reader('alunos.csv', '105473').get_name(), 'Gabriela Pereira Araujo')

        self.assertEqual(Student.csv_reader('alunos.csv', '123456'), 0)


    def test_student_uffmail_options_generator(self):
		# Tests uffmail array returned by the method uffmail_options_generator()
        reset_file()
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').uffmail_options_generator(), 0)

        self.assertEqual(Student.csv_reader('alunos.csv', '101369').uffmail_options_generator(), 0)

        self.assertEqual(Student.csv_reader('alunos.csv', '100591').uffmail_options_generator(), [
            'lucasoliveirabarros@id.uff.br',
            'lucasoliveira@id.uff.br',
            'lucasbarros@id.uff.br',
            'lucas_oliveira@id.uff.br',
            'lucas_barros@id.uff.br',
            'loliveirabarros@id.uff.br',
            'lobarros@id.uff.br',
            'lucasobarros@id.uff.br',
            'lucasob@id.uff.br',
            'lucasoliveirab@id.uff.br'
        ])


    @mock.patch('student.input', create=True)
    def test_student_uffmail_creator(self, mocked_input):
        # Tests uffmail created by the method uffmail_creator()
        reset_file()
        file = 'alunos.csv'

        student = Student.csv_reader("alunos.csv", '109647')
        options = student.uffmail_options_generator()
        mocked_input.side_effect = ['7']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, file), 'gsribeiro@id.uff.br')

        student = Student.csv_reader("alunos.csv", '111111')
        options = student.uffmail_options_generator()
        mocked_input.side_effect = ['12']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, file), 'alfabravocharlied@id.uff.br')

        student = Student.csv_reader("alunos.csv", '222222')
        options = student.uffmail_options_generator()
        mocked_input.side_effect = ['1']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, file), 'joaoameliocorintio@id.uff.br')

        student = Student.csv_reader("alunos.csv", '333333')
        options = student.uffmail_options_generator()
        mocked_input.side_effect = ['a']
        mocked_input.side_effect = ['@']
        mocked_input.side_effect = ['*']
        mocked_input.side_effect = ['/']
        mocked_input.side_effect = ['+']
        mocked_input.side_effect = ['.']
        mocked_input.side_effect = ['!']
        mocked_input.side_effect = ['=']
        mocked_input.side_effect = ['5.5']
        mocked_input.side_effect = ['3,1']
        mocked_input.side_effect = ['5']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, file), 'nome_ccccc@id.uff.br')

    def test_password_sender(self):
		# Tests the return of the method passord_sender()
        reset_file()
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').password_sender(), 'Success')

        self.assertEqual(Student.csv_reader('alunos.csv', '100406').password_sender(), 'err - inexistent uffmail')


if __name__ == '__main__':
    main()
