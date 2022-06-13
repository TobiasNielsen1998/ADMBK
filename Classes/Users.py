from stdnum.dk import cpr
from AdmEmployee import AdmEmployee
from Teacher import Teacher


class Users:
    """
    class to represent a list of Employees
    """

    def __init__(self):
        self.admemployees = []
        self.teachers = []

    def append_admemp(self, emp :AdmEmployee):
        """
        Appends all amdemps to list, checks that they have all info needed
        """
        emp = AdmEmployee(emp[0],emp[1],emp[2],emp[3],emp[4])
        if emp not in self.admemployees:
            self.admemployees.append(emp)
    
    def append_teacher(self, teacher :Teacher):
        """
        Appends all teachers to list, checks that they have all info needed
        """
        teacher = Teacher(teacher[0],teacher[1],teacher[2],teacher[3],teacher[4])
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def get_admemps(self):
        """
        Returns list of admemps
        """
        return self.admemployees
    

    def get_teachers(self): 
        """
        Returns list of teachers
        """
        return self.teachers