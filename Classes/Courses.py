import mysql.connector
from datetime import *
from Course import Course


class Courses:
    """
    class to represent a list of Courses
    """

    def __init__(self):
        self.courses = []

    def append_course(self, course :Course):
        """
        Appends course to list of courses
        - makes a empty list for schedule
        """
        if course not in self.courses:
            if isinstance(course,Course) is True:
                self.courses.append(course)
            else:
                self.courses.append(course + ([],))

    def get_courses(self):
        """
        Gets all courses appenden to list of courses
        - appends schedule to given course
        """
        for i in self.courses:
            i[5].clear()
        temp_list = []
        temp_list1 = []
        connection = mysql.connector.connect(host='mysql-db.caprover.diplomportal.dk',
                                            database='s206016',
                                            user='s206016',
                                            password='tgbF5PriPdYWNJquI2MvL')
        cursor = connection.cursor()
        cursor.execute('SELECT CourseDays, CourseDayEnd, CourseID FROM Schedules')

        st = 0
        sl = 3
        for i in cursor:
            for x in i:
                temp_list.append(str(x))
        for i in range(0,len(temp_list),3):
                temp_list1.append(' - '.join(temp_list[st:sl]).strip())
                st+=3
                sl+=3
        for i in temp_list1:
            for x in self.courses:
                if str(x[0]) == i[-3:]:
                    x[5].append(i[:-6])
                    x[5].sort()
        return self.courses