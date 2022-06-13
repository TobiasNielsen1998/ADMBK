from PyQt6 import QtWidgets, uic
from AdmEmpManaging import AdmEmpManaging

class loginAdmEmp(QtWidgets.QWidget):
    """
    GUI for Administrative employees login
    """
    def __init__(self, employees :list, courses :list):
        """
        Defining required class items
        """
        super(loginAdmEmp, self).__init__()
        uic.loadUi('UI/LoginAdmEmpGUI.ui', self) #Path for LoginAdmEmpGUI.ui
        
        self.list_Courses = courses
        self.employees = employees
        self.adm_emp = employees.get_admemps()
        self.usernames = []
        self.cprs = []
        for a in self.adm_emp:
            self.usernames.append(a.get_user_id())
            self.cprs.append(a.get_cpr_number())

        self.pushButton_2.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.quit)
        self.show()

    def login(self):
        """
        Defining the login button - Logs-in if correct username and password
        """
        if self.lineEdit.text() in self.usernames and self.lineEdit_2.text() in self.cprs:
            print("Correct")
            """
            App Administarive request managing
            """
            self.manage_CourseSchedule = AdmEmpManaging(self.list_Courses,self.employees)
            self.manage_CourseSchedule.show()
            self.close()
        else:
            print("Invalid")
            self.show()
    
    def quit(self):
        """
        Defining the Quit button - quits the whole script
        """
        print('Quit button pressed!')
        quit()