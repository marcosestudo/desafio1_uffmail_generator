import unittest
from student import Student

# To run tests
# >>> python -m unittest
# or
# >>> python -m unittest -v
class TestStudentMethods(unittest.TestCase):

    def test_student_name(self):
		# Tests if the student returned by the Student.csv_reader() method is correct by name
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').get_name(), 'Luiza Fernandes Ferreira')

        self.assertEqual(Student.csv_reader('alunos.csv', '100503').get_name(), 'Vitor Fernandes Costa')

        self.assertEqual(Student.csv_reader('alunos.csv', '105473').get_name(), 'Gabriela Pereira Araujo')

        self.assertEqual(Student.csv_reader('alunos.csv', '123456'), 0)


    def test_student_uffmail_generator(self):
		# Tests uffmail array returned by the method uffmail_generator()
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').uffmail_generator(), 0)

        self.assertEqual(Student.csv_reader('alunos.csv', '101369').uffmail_generator(), 0)

        self.assertEqual(Student.csv_reader('alunos.csv', '100591').uffmail_generator(), [
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


    def test_student_uffmail_creator(self):
		# Tests uffmail array returned by the method uffmail_generator()
        student = Student.csv_reader("alunos.csv", '111111')
        options = student.uffmail_generator()
        self.assertEqual(student.uffmail_creator(options, 11), 'alfabravocharlied@id.uff.br')

        student = Student.csv_reader("alunos.csv", '109647')
        options = student.uffmail_generator()
        self.assertEqual(student.uffmail_creator(options, 0), 'gabrielasantosribeiro@id.uff.br')

        student = Student.csv_reader("alunos.csv", '100591')
        options = student.uffmail_generator()
        self.assertEqual(student.uffmail_creator(options, 9), 'lucasoliveirab@id.uff.br')


if __name__ == '__main__':
    unittest.main()
