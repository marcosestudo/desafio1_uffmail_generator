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
		# Tests uffmail created by the method uffmail_creator() 
        file = "alunos.csv"

        student = Student.csv_reader(file, '111111')
        self.assertEqual(student.uffmail_creator(11, file), 'alfabravocharlied@id.uff.br')

        student = Student.csv_reader(file, '109647')
        self.assertEqual(student.uffmail_creator(0, file), 'gabrielasantosribeiro@id.uff.br')

        student = Student.csv_reader(file, '100591')
        self.assertEqual(student.uffmail_creator(9, file), 'lucasoliveirab@id.uff.br')


    def test_password_sender(self):
		# Tests the return of the method passord_sender()
        self.assertEqual(Student.csv_reader('alunos.csv', '105794').password_sender(), 'Success')

        self.assertEqual(Student.csv_reader('alunos.csv', '100406').password_sender(), 'err - inexistent uffmail')


if __name__ == '__main__':
    unittest.main()
