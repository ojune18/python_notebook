from employee import Employee
from datetime import datetime
from employee_exception import RejoiningException



class PermanentEmployee(Employee):

    def __init__(self, _name, _department):
        super().__init__(_name, _department)

    def is_rejoinee(self):
        """returns True if employee has rejoined otherwise False"""
        return len(self._start_date) > 1

    def process_employee_exit(self):
        """Process the Exit of employee"""
        if self.is_employee_serving():
            self._end_date.append(datetime.now().isoformat())

            print(f"Successfully processed exit for employee {self.name} on" \
                      f"{self._end_date[-1]}\nWe wish {self.name} for future endeavours")
            return
        raise RejoiningException("Employee not in service. Cannot process exit.")
