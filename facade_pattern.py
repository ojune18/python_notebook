class Student:

    def __init__(self, name, standard):
        self.name = name
        self.role = Role()

class Role():
    pass


class Monitor(Student):

    def __init__(self, name, standard):
        super().__init__(name, standard)
        self.monitor = True

    def perform_duty(self):
        return 'OK'

    @staticmethod
    def convert_to_student(name,standard):
        return  Student(name,standard)


class Classroom:

    def __init__(self, student_arr, standard):
        self.students = student_arr
        self.attendence = {}
        self.standard = standard

    def count_students(self):
        return len(self.students)

    def take_attendence(self):
        item = len(self.students)
        while item > 0:
            self.attendence[self.students[item]] = input("Type 'yes' or 'no' to mark attendence\n")
            item -= 1


class ClassroomExists(Exception):
    pass


class MonitorExists(Exception):
    pass


class SchoolSystemFacade:

    def __init__(self):
        self.student_arr = []
        self.classrooms = {}

    def _check_classroom_exists(self, standard):
        classroom = self.classrooms.get(standard, None)
        if classroom is not None:
            return classroom
        raise KeyError(f'Classroom with {standard} does not exists')

    def create_student(self, name, standard):
        student = Student(name, standard)
        self.student_arr.append(student)
        return student

    def create_monitor(self, name, standard):
        self._check_classroom_exists(standard)
        monitor_arr = [x for x in self.classrooms[standard] if type(x) == Monitor]
        if len(monitor_arr) == 0:
            monitor = Monitor(name, standard)
            self.student_arr.append(monitor)
            return Monitor
        raise MonitorExists("Monitor Exists on class.")

    def create_classroom(self, standard):
        classroom = self.classrooms.get(standard, None)
        if classroom is None:
            students = [x for x in self.classrooms if x.standard == standard]
            classroom = Classroom(students, standard)
            self.classrooms[standard] = classroom
            return classroom
        raise ClassroomExists(f'Classroom with standard {standard} already exists')

    def get_student_names(self, standard):
        classroom = self._check_classroom_exists(standard)
        return [x.name for x in classroom.students]

    def get_class_monitor(self, standard):
        classroom = self._check_classroom_exists(standard)
        return [x for x in classroom.students if type(x) == Monitor]

    def discipline_class(self, standard):
        monitor = self.get_class_monitor(standard)
        monitor[0].perform_duty()

    def change_monitor(self, name, standard):
        self._check_classroom_exists(standard)
        monitor_arr = self.get_class_monitor(standard)
        if len(monitor_arr) > 0:
            self.classrooms[standard].students.remove(monitor_arr[0])


s = SchoolSystemFacade()
d = {'1': 'Create Student'}
