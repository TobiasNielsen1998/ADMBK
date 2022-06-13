from datetime import *
from PyQt6 import QtWidgets, uic
import mysql.connector
from Requests import Requests

class TeacherRequest(QtWidgets.QWidget):
    """
    GUI for teacher requests
    """
    def __init__(self, list_schedule_before: list):
        """
        Define class requirments
        """
        super(TeacherRequest, self).__init__()
        uic.loadUi('UI/TeacherRequestGUI.ui', self) #Path for TeacherRequestsGUI.ui

        self.list_Courses = list_schedule_before
        self.comboBox.addItems(self.get_courses())
        self.ImportButton.clicked.connect(self.get_course_info)
        self.pushButtonOK.clicked.connect(self.create_request)
        self.listWidget_4.addItems(self.get_requestes())
        self.pushButtonDone.clicked.connect(self.done_requesting)
        self.get_course_info()
        self.show()

    def get_courses(self):
        """
        Adding combobox item
        """
        items = [str(list(i[0:5])).translate(str.maketrans('', '', "'[]"))for i in self.list_Courses]
        return items

    def get_requestes(self):
        """
        Adding requested items from the sql database to the list widget
        """
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        cursor.execute('SELECT Requests, RequestStatus, CourseID, CourseName, CourseDays, CourseDayEnd, CourseFaculty, CourseRoom, CourseTeacher, CourseNote FROM Requests')
        temp_list = []
        items = []
        st = 0
        sl = 10
        for i in cursor:
            for x in i:
                temp_list.append(str(x))
        for i in range(0,len(temp_list),10):
            items.append('\n --'.join(temp_list[st:sl]).strip())
            st+=10
            sl+=10
            Requests().schedule_request(i)
        return items
    
    def get_course_info(self):
        """
        Defining import button process - importing the chosen combobox item to the QLines
        """
        print("Import button pressed!")

        self.CourseNameLineEdit_4.setText(f'{self.comboBox.currentText().split(",")[1]}'.strip("][' '"))
        self.CourseIDLineEdit_4.setText(f'{self.comboBox.currentText().split(",")[0]}'.strip("][' '"))
        self.CourseFacultyLineEdit_4.setText(f'{self.comboBox.currentText().split(",")[2]}'.strip("][' '"))
        self.CourseRoomLineEdit_4.setText(f'{self.comboBox.currentText().split(",")[3]}'.strip("][' '"))
        self.CourseTeacherLineEdit_4.setText(f'{self.comboBox.currentText().split(",")[4]}'.strip("][' '"))

        """
        Adding current schedule from the sql database to the list widget
        """
        self.listWidget.clear()
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        query = 'SELECT CourseName, CourseDays, CourseDayEnd, CourseFaculty, CourseRoom FROM Schedules WHERE CourseID = %s'
        val = (f'{self.comboBox.currentText().split(",")[0]}'.strip("][' '"),)
        cursor.execute(query, val)
        temp_list = []
        items = []
        st = 0
        sl = 5
        for i in cursor:
            for x in i:
                temp_list.append(str(x))
        for i in range(0,len(temp_list),5):
            items.append('\n --'.join(temp_list[st:sl]).strip())
            st+=5
            sl+=5
        self.listWidget.addItems(items)
        self.listWidget.sortItems()

    def create_request(self):
        """
        Defining OK button - Appends the created request to the sql-database
        """
        print("OK button pressed!")

        course_name = self.CourseNameLineEdit_4.text()
        course_id = int(self.CourseIDLineEdit_4.text())
        course_faculty = self.CourseFacultyLineEdit_4.text()
        course_room = int(self.CourseRoomLineEdit_4.text())
        course_day_end = time.fromisoformat(self.timeEdit.text())
        course_teacher = self.CourseTeacherLineEdit_4.text()
        course_days =  datetime.fromisoformat(self.CourseDayLineEdit_4.text())
        course_note =  str(self.CourseNotetextEdit.toPlainText())

        try:
            connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                             database='s206016',
                                               user='s206016',
                                             password='tgbF5PriPdYWNJquI2MvL')
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO Requests (RequestStatus, CourseID, CourseName, CourseDays, CourseDayEnd, CourseFaculty, CourseRoom, CourseTeacher, CourseNote)
                                            VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"""

            record = ("Pending" ,course_id, course_name, course_days, course_day_end, course_faculty, course_room, course_teacher, course_note)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record INSERTED successfully into sql table")
            note_clean = self.findChildren(QtWidgets.QTextEdit)
            for i in note_clean:
                i.clear()
        except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))
                print("Arrgh! Something went wrong!!", error)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Input error")
                msg.setText("Badly formatted input!")
                msg.setDetailedText(str(error))
                msg.exec()
                line_edits = self.findChildren(QtWidgets.QLineEdit)
                for field in line_edits:
                    field.clear()
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        self.listWidget_4.addItems([self.get_requestes()[-1]])

    def done_requesting(self):
        """
        Defining the done button - completes the made changes in the session
        """
        print('Done button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Exit form?", "Are you done requesting all your changes?")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            self.close()
        else:
            print("No!")