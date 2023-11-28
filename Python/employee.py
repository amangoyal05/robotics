import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Aman', 'Goyal')
emp_3 = Employee('Jane', 'Doe')