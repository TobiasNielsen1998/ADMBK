"""
Inspired by cookbook
"""
from PyQt6 import QtWidgets, uic
import mysql.connector
from datetime import *
from CoursesToXML import *
from XMLtoCourses import *


class AdmEmpManaging(QtWidgets.QWidget):
    """
    GUI for administarive employee request managing
    """
    def __init__(self, list_schedule: list, employees: list):
        """
        Define class requirments
        """
        super(AdmEmpManaging, self).__init__()
        uic.loadUi('UI/AdmEmpManagingGUI.ui', self) #Path for AdmEmpManagingGUI.ui

        self.teachers = employees
        self.list_Courses = list_schedule
        self.comboBox.addItems(self.get_courses())
        self.listWidget_4.addItems(self.get_requestes())
        self.ImportButton.clicked.connect(self.get_course_info)
        self.pushButtonOK.clicked.connect(self.update_request_status)
        self.pushButtonChange.clicked.connect(self.make_course_changes)
        self.pushButtonCancel.clicked.connect(self.quit_managing)
        self.pushButtonXML.clicked.connect(self.create_validate_course_xml)
        self.get_course_info()
        self.show()

    def get_courses(self):
        """
        Adding combobox item
        """
        items = [str(list(i[0:5])).translate(str.maketrans('', '', "'[]"))for i in self.list_Courses.get_courses()]
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
        cursor.execute('SELECT Requests, RequestStatus, CourseID, CourseName, CourseDays, CourseDayEnd, CourseFaculty, CourseRoom, CourseTeacher, CourseNote FROM Requests WHERE RequestStatus = "Pending"')
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

    def update_request_status(self):
        """
        Defining OK button - Removes requests, and creats notification of updated state
        """
        print("OK button pressed!")
        x = self.listWidget_4.currentItem().text()
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        query = 'UPDATE Requests SET RequestStatus = %s WHERE Requests = %s'

        button = QtWidgets.QMessageBox.question(self, "Accept request?", "Do you want to ACCEPT this request? \nPress YES to ACCEPT \nPress NO to REJECT")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Accepted!")
            val = ("Accepted", x.splitlines()[0],)
            cursor.execute(query, val)
            connection.commit()
        elif button == QtWidgets.QMessageBox.StandardButton.No:
            print("Rejected!")
            val = ("Rejected", x.splitlines()[0],)
            cursor.execute(query, val)
            connection.commit()
        else:
            print("Closed!")
            
        self.listWidget_4.currentItem().setHidden(True)
        print("Request Updated")

    def make_course_changes(self):
        """
        Defining the Make change button - completes the made changes in the session
        """
        print('Make-change button pressed!')

        course_name = self.CourseNameLineEdit_4.text()
        course_id = int(self.CourseIDLineEdit_4.text())
        course_faculty = self.CourseFacultyLineEdit_4.text()
        course_room = int(self.CourseRoomLineEdit_4.text())
        course_day_end = time.fromisoformat(self.timeEdit_2.text())
        course_days =  datetime.fromisoformat(self.CourseDayLineEdit_4.text())

        if self.checkBoxAdd.isChecked():
            try:
                connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO Schedules (CourseID, CourseDays, CourseDayEnd, CourseName, CourseFaculty, CourseRoom)
                                                VALUES (%s, %s, %s, %s, %s, %s)"""

                record = (course_id, course_days, course_day_end, course_name, course_faculty, course_room)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record INSERTED successfully into sql table")
            except mysql.connector.Error as error:
                    print("Failed to insert into MySQL table {}".format(error))
                    print("Arrgh! Something went wrong!!", error)
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Input error")
                    msg.setText("Badly formatted input!")
                    msg.setDetailedText(str(error))
                    msg.exec()
                    line_edits = self.findChildren(QtWidgets.QLineEdit)
                    # Loop over the fields and clear them
                    for field in line_edits:
                        field.clear()
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
        elif self.checkBoxDelete.isChecked():
            try:
                connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                                database='s206016',
                                                user='s206016',
                                                password='tgbF5PriPdYWNJquI2MvL')
                cursor = connection.cursor()
                mySql_insert_query = """DELETE FROM Schedules WHERE CourseID = %s AND CourseDays = %s"""
                record = (course_id, course_days)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record DELETED successfully from sql table")
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

        button = QtWidgets.QMessageBox.information(self, "Make this change", "This day will be added/deleted")
        if button == QtWidgets.QMessageBox.StandardButton.Ok:
            print("Yes!")
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            for field in line_edits:
                field.clear()
        else:
            print("No!")
        self.listWidget.clear()

    def quit_managing(self):
        """
        Defining the Quit button - saves and exits the script
        """
        print('Done button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Exit form?", "Are you done making changes?")
        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            self.close()
        else:
            print("No!")

    def create_validate_course_xml(self):
        """
        XML
        """
        print("\n*** Write the courselist to courses.xml ***\n")
        CoursesToXml(self.list_Courses.get_courses(), self.teachers.get_teachers()).write_file()

        print("\n*** Reading the xml file ***\n")

        course_list = XmlToCourses('XML/courses.xml').parseXML()
        print("\n*** Checking documents: ***\n")

        dtd = etree.DTD(open('courses.dtd'))
        print("Check generated courses.xml",dtd.validate(etree.parse('XML/courses.xml')))
        print("\n*** ADMBK DONE: ***\n")