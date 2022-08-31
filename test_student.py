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
    file = 'alunos.csv'


    def test_student_name(self):
		# Tests if the student returned by the Student.csv_reader() method is correct by name
        reset_file()


        self.assertEqual(Student.csv_reader(self.file, '105794').get_name(), 'Luiza Fernandes Ferreira')

        self.assertEqual(Student.csv_reader(self.file, '100503').get_name(), 'Vitor Fernandes Costa')

        self.assertEqual(Student.csv_reader(self.file, '105473').get_name(), 'Gabriela Pereira Araujo')

        self.assertEqual(Student.csv_reader(self.file, '123456'), 0)


    def test_student_uffmail_options_generator(self):
		# Tests uffmail array returned by the method uffmail_options_generator()
        reset_file()
        

        self.assertEqual(Student.csv_reader(self.file, '105794').uffmail_options_generator(self.file), 0)

        self.assertEqual(Student.csv_reader(self.file, '101369').uffmail_options_generator(self.file), 0)

        self.assertEqual(Student.csv_reader(self.file, '100591').uffmail_options_generator(self.file), [
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
        

        student = Student.csv_reader("alunos.csv", '109647')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['7']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'gsribeiro@id.uff.br')

        student = Student.csv_reader("alunos.csv", '111111')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['12']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'alfabravocharlied@id.uff.br')

        student = Student.csv_reader("alunos.csv", '222222')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['1']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'joaoameliocorintio@id.uff.br')

        student = Student.csv_reader("alunos.csv", '333333')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['a', '@', '*', '/', '+', '.', '!', '=', '5.5', '3,1', '5']
        chosen_option = student.options_printer(options)
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nome_ccccc@id.uff.br')


    def test_password_sender(self):
		# Tests the return of the method passord_sender()
        reset_file()
        

        self.assertEqual(Student.csv_reader(self.file, '105794').password_sender(), 'Success')

        self.assertEqual(Student.csv_reader(self.file, '100406').password_sender(), 'err - inexistent uffmail')


    @mock.patch('student.input', create=True)
    def test_student_uffmail_options_generator_email_repetition(self, mocked_input):
        # Tests to see the output from uffmail_options_generator to check if repeated uffmails are generated
        reset_file()

        student = Student.csv_reader(self.file, '444444')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['1']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nomemuitocomum@id.uff.br',
            'nomemuito@id.uff.br',
            'nomecomum@id.uff.br',
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
            'nomemc@id.uff.br',
            'nomemuitoc@id.uff.br'
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomemuitocomum@id.uff.br')

        student = Student.csv_reader(self.file, '555555')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['1']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nomemuito@id.uff.br',
            'nomecomum@id.uff.br',
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
            'nomemc@id.uff.br',
            'nomemuitoc@id.uff.br'
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomemuito@id.uff.br')

        student = Student.csv_reader(self.file, '666666')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['1']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nomecomum@id.uff.br',
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
            'nomemc@id.uff.br',
            'nomemuitoc@id.uff.br'
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomecomum@id.uff.br')

        student = Student.csv_reader(self.file, '777777')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['7']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
            'nomemc@id.uff.br',
            'nomemuitoc@id.uff.br'
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomemuitoc@id.uff.br')

        student = Student.csv_reader(self.file, '888888')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['6']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
            'nomemc@id.uff.br'
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomemc@id.uff.br')

        student = Student.csv_reader(self.file, '999999')
        options = student.uffmail_options_generator(self.file)
        mocked_input.side_effect = ['5']
        chosen_option = student.options_printer(options)
        self.assertEqual(options, [
            'nome_muito@id.uff.br',
            'nome_comum@id.uff.br',
            'nmuitocomum@id.uff.br',
            'nmcomum@id.uff.br',
            'nomemcomum@id.uff.br',
        ])
        self.assertEqual(student.uffmail_creator(chosen_option, self.file), 'nomemcomum@id.uff.br')


if __name__ == '__main__':
    main()
