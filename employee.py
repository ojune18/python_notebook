"""This is employee module on OOPS principle"""

from datetime import datetime


class Employee():
    """This is Employee Base class which provides various methods and features
    name : Employee Name
    department: An array of department strings
    manager: Set or get current manager of Employee
    projects: An array of project strings
    """
    allowed_rejoin = 3
    instance_count = 0

    def __init__(self, _name, _department):
        self._name = ''  # str
        self._department = []  # Department
        self._manager = ''  # Employee
        self._projects = []  # [Project]
        self._start_date = [datetime.now().isoformat()]
        self._end_date = []
        Employee.instance_count = +1
        self._id = Employee.instance_count

    @property
    def name(self):
        """getter for employee name"""
        return self._name

    @name.setter
    def name(self, val):
        """setter for employee name"""
        self._name = val

    @property
    def emp_id(self):
        """getter for emp_id"""
        return self._id

    @emp_id.setter
    def emp_id(self, val):
        """Setter for emp_id"""
        self._id = val

    @property
    def department(self):
        """getter for Employee department"""
        return self._department[:]

    @department.setter
    def department(self, val):
        """setter for employee department"""
        self._department = val

    @property
    def manager(self):
        """getter for employee manager"""
        return self._manager

    @manager.setter
    def manager(self, val):
        self._manager = val

    @property
    def projects(self):
        """getter for emp projects"""
        return self._projects[:]

    def add_project(self, val):
        """Add projects for employee"""
        self._projects.append(val)

    def remove_project(self, val):
        """Remove employee from a project"""
        if val in self._projects:
            self._projects.remove(val)
            return self.projects
        raise ValueError('Project not present in assigned projects')

    def current_project(self):
        """returns current project of employee"""
        return self._projects[-1]

    def is_employee_serving(self):
        """returns True if employee is serving otherwise False"""
        return len(self._start_date) != len(self._end_date)

    def latest_start_date(self):
        """returns the last start date of employee"""
        return self._start_date[-1]

    def get_service_period(self):
        """Prints the serving terms of employee"""
        for item in range(0, len(self._start_date)):

            if item > (len(self._end_date) - 1):
                print(f"Employee is serving from {self._start_date[item]}")

            else:
                print(f"Employee served from {self._start_date[item]} to {self._end_date[item]}")

    @staticmethod
    def class_method():
        print('In class method')
