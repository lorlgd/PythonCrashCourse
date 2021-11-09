from Chapter11.Exercises.Employee import Employee
import unittest


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        """
        Create an employee and a set of annual raises.
        """
        self.my_employee = Employee('Javier', 'Ramirez', '1000')
        self.salary_raise = '100_000_000'

    def test_give_default_raise(self):
        """Test Employee class with default increment"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 6000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.salary_raise)
        self.assertEqual(self.my_employee.annual_salary, 100_001_000)


if __name__ == '__main__':
    unittest.main()
