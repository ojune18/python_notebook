"""Module for temporary employee in the company"""

from employee import Employee
from employee_exception import ContractException
from datetime import datetime

LISTED_CONTRACT_AGENCY = {'Securitas': {'A': 100, 'B': 200, 'C': 500},
                          'Xian': {'A': 1000, 'B': 2000, 'C': 5000}}


class TemporaryEmployee(Employee):
    """Class for a Contractor employee"""
    third_party = True

    def __init__(self, _name, _department):
        super().__init__(_name, _department)
        self._contract_agency = ''
        self._contract_term = ''
        self._grade = ''

    @property
    def contract_agency(self):
        """getter for contract_agency"""
        return self._contract_agency

    @contract_agency.setter
    def contract_agency(self, val):
        """setter for contract_agency"""
        if val in LISTED_CONTRACT_AGENCY:
            self._contract_agency = val
        raise ValueError(f'Permissible agencies are {LISTED_CONTRACT_AGENCY.keys()}')

    @property
    def contract_term(self):
        """getter for contract_term"""
        return self._contract_term

    @contract_term.setter
    def contract_term(self, val):
        """setter for contract_term"""
        if self.grade and self.contract_agency:
            if val > self._calculate_term(self.grade):
                self._contract_term = val
                return
            raise ValueError('Contract term requirements are not met')
        raise ContractException('Grade and Agency of contractor are needed to be defined first')

    @property
    def grade(self):
        """getter for grade"""
        return self._grade

    def change_contract_grade_term(self, args_grade, args_term):
        """Chnages the contract grade and term of employee"""
        if args_grade and args_term and self.contract_agency and isinstance(args_term, (float, int)):
            if args_grade in LISTED_CONTRACT_AGENCY[self.contract_agency].keys() and args_grade != self.grade:
                if args_term > self._calculate_term(args_grade):
                    self.grade = args_grade
                    self.contract_term = args_term
                    return self
                raise ValueError('Cannot change grade as term passed did not meet requirements')
            raise ValueError(
                'Cannot change the grade as either it is not present with agency or the grade the same as previous')
        raise ValueError('Not proper values passed to the method')

    def _calculate_term(self, args_grade):
        """Private method to check if contract term is as per business rules"""
        return LISTED_CONTRACT_AGENCY[self.contract_agency][args_grade] % 100 + 1

    def remove_project(self, val):
        if self.is_employee_serving():
            if val in self.projects:
                self.projects.remove(val)


    def process_emp_exit(self):
        super()._end_date.append(datetime.now().isoformat())




t_emp = TemporaryEmployee('Rajiv', 'Dept-A')

t_emp.get_service_period()
t_emp.add_project('ui')
print(help(t_emp))

