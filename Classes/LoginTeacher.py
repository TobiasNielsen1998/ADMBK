from PyQt6 import QtWidgets, uic
from TeacherRequest import TeacherRequest

class loginTeacher(QtWidgets.QWidget):
    """
    GUI for teacher login
    """
    def __init__(self, teachers :list, courses):
        """
        Defining required class items
        """
        super(loginTeacher, self).__init__()
        uic.loadUi('UI/LoginTeacherGUI.ui', self) #Path for LoginTeacherGUI.ui
        
        self.list_Courses = courses
        self.teachers = teachers
        self.usernames = []
        self.cprs = []
        for t in self.teachers:
            self.usernames.append(t.get_user_id())
            self.cprs.append(t.get_cpr_number())

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
            App Teacher requests
            """
            self.edit_CourseSchedule = TeacherRequest(self.list_Courses.get_courses())
            self.edit_CourseSchedule.show()
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