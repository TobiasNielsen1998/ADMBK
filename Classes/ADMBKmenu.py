from PyQt6 import QtWidgets, uic
import mysql.connector
from LoginTeacher import loginTeacher
from Users import Users
from Courses import Courses
from LoginAdmEmp import loginAdmEmp
from SqlDatabase import SqlDatabase


class ADMBKmenu(QtWidgets.QWidget):
    """
    GUI for administarive employee request managing
    """
    """
    Setting up ADMBK - press "y" if you want to reset database
    """
    print("Do you want to restart the ADMBK database? -y/n")
    userinput = input()
    if userinput == "y":
        drop_req = SqlDatabase("DROP TABLE Requests")
        drop_req.drop_table()
        print("Requests DROPED")
        drop_sch = SqlDatabase("DROP TABLE Schedules")
        drop_sch.drop_table()
        print("Schedule DROPED")
        drop_adm = SqlDatabase("DROP TABLE AdmEmployees")
        drop_adm.drop_table()
        print("AdmEmployees DROPED")
        drop_cou = SqlDatabase("DROP TABLE Courses")
        drop_cou.drop_table()
        print("Courses DROPED")
        drop_tec = SqlDatabase("DROP TABLE Teachers")
        drop_tec.drop_table()
        print("Teachers DROPED")
        drop_usr = SqlDatabase("DROP TABLE Users")
        drop_usr.drop_table()
        print("Users DROPED")
        execute_ddl = SqlDatabase("SQL/ADMBKddl.sql") #PATH for ADMBKddl.sql
        execute_ddl.db_ddl()
        print("Users CREATED & Teachers CREATED & Courses CREATED & Schedules CREATED & Requests CREATED & AdmEmplyees CREATED")
        execute_usr_dml = SqlDatabase("SQL/ADMBKusersDML.sql") #PATH for ADMBKusersDML.sql
        execute_usr_dml.db_dml()
        print("INSERTED DATA INTO Users")
        execute_teacher_dml = SqlDatabase("SQL/ADMBKteachersDML.sql") #PATH for ADMBKteachersDML.sql
        execute_teacher_dml.db_dml()
        print("INSERTED DATA INTO Teachers")
        execute_courses_dml = SqlDatabase("SQL/ADMBKcoursesDML.sql") #PATH for ADMBKcoursesDML.sql
        execute_courses_dml.db_dml()
        print("INSERTED DATA INTO Courses")
        execute_schedules_dml = SqlDatabase("SQL/ADMBKscheduleDML.sql") #PATH for ADMBKschedulesDML.sql
        execute_schedules_dml.db_dml()
        print("INSERTED DATA INTO Schedules")
        execute_admemp_dml = SqlDatabase("SQL/ADMBKadmEmpDML.sql") #PATH for ADMBKadmEmpDML.sql
        execute_admemp_dml.db_dml()
        print("INSERTED DATA INTO AdmEmployee")

    def __init__(self):
        """
        Define class requirments
        """
        super(ADMBKmenu, self).__init__()
        uic.loadUi('UI/ADMBKmenuGUI.ui', self) #Path for AdmEmpManagingGUI.ui
        self.list_employees = Users()
        """
        Teacher
        """
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Teachers')
        
        for i in cursor:
            self.list_employees.append_teacher(i)
        
        """
        AdmEmployee
        """
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM AdmEmployees')
        
        for i in cursor:
            self.list_employees.append_admemp(i)

        """
        Schedule
        """
        self.list_Courses = Courses()

        """
        Courses
        """    
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Courses')

        for i in cursor:
            self.list_Courses.append_course(i)
        
        self.pushButtonLoginTeacher_3.clicked.connect(self.teacher_menu)
        self.pushButtonLoginAdmEmp_3.clicked.connect(self.admemp_menu)
        self.show()

    def teacher_menu(self):
        """
        Login teachers
        """
        print("Login by typing one of the UserIDs and the associated UserCpr!")
        print("Teacher 1 userID: slg250")
        print("Teacher 1 userCPR: 2110625629")
        print("Teacher 2 userID: kap111")
        print("Teacher 2 userCPR: 2110625629")
        print("Teacher 3 userID: nak999")
        print("Teacher 3 userCPR: 2110625629")
        self.login = loginTeacher(self.list_employees.get_teachers(), self.list_Courses)
        self.login.show()
        self.close()

    def admemp_menu(self):
        """
        Login Administrativ employees
        """
        print("Login by typing one of these User IDs and the associated User Cpr!")
        print("AdmEmp 1 userID: dew121")
        print("AdmEmp 1 userCPR: 2110625629")
        print("AdmEmp 2 userID: uyj212")
        print("AdmEmp 1 userCPR: 2110625629")
        self.login = loginAdmEmp(self.list_employees, self.list_Courses)
        self.login.show()
        self.close()