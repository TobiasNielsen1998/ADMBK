import unittest
from Teacher import *
from AdmEmployee import *
from datetime import *
from Course import *
from itertools import *

tec = Teacher("Anders Andersen", "dff199", "2110625629", "+4512121212", "anders.andersen@company.com")
adm = AdmEmployee("Morten Hansen", "dew121", "211062-5629", "+4522313263", "morten.hansen@company.com")
sch = Course(342,"Sundhed", "KU", 1, tec)


class TestTeacherMethods(unittest.TestCase):
    """Unit-test TeacherClass"""
    def test_name(self):
        self.assertEqual(tec.get_name(), "Anders Andersen")
        tec.set_name("Anders Lundberg") #Ændre navn
        self.assertEqual(tec.get_name(), "Anders Lundberg")

        self.assertEqual(tec.get_user_id(), "dff199")
        tec.set_user_id("egt202") #Ændre UserID
        self.assertEqual(tec.get_user_id(), "egt202")

        self.assertEqual(tec.get_cpr_number(), "2110625629")
        tec.set_cpr_number("211062-5629") #Ændre CPR
        self.assertEqual(tec.get_cpr_number(), "2110625629")

        self.assertEqual(tec.get_phone(), "+4512121212")
        tec.set_phone("+4589783245") #Ændre tlf. nr.
        self.assertEqual(tec.get_phone(), "+4589783245")

        self.assertEqual(tec.get_email(), "anders.andersen@company.com")
        tec.set_email("anders.lundberg@company.com") #Ændre email
        self.assertEqual(tec.get_email(), "anders.lundberg@company.com")

class TestAdmEmployeeMethods(unittest.TestCase):
    """Unit-test AdmEmployeeClass"""
    def test_name(self):
        self.assertEqual(adm.get_name(), "Morten Hansen")
        adm.set_name("Morten Lundberg") #Ændre navn
        self.assertEqual(adm.get_name(), "Morten Lundberg")

        self.assertEqual(adm.get_user_id(), "dew121")
        adm.set_user_id("fre322") #Ændre UserID
        self.assertEqual(adm.get_user_id(), "fre322")

        self.assertEqual(adm.get_cpr_number(), "2110625629")
        adm.set_cpr_number("2110625629") #Ændre CPR
        self.assertEqual(adm.get_cpr_number(), "2110625629")

        self.assertEqual(adm.get_phone(), "+4522313263")
        adm.set_phone("+4539480598") #Ændre tlf. nr.
        self.assertEqual(adm.get_phone(), "+4539480598")
        
        self.assertEqual(adm.get_email(), "morten.hansen@company.com")
        adm.set_email("morten.lundberg@company.com") #Ændre email
        self.assertEqual(adm.get_email(), "morten.lundberg@company.com")

class TestScheduleMethods(unittest.TestCase):
    """Unit-test ScheduleClass"""
    def test_name(self):
        self.assertEqual(sch.get_course_name(), "Sundhed")
        sch.set_course_name("Programmering") #Ændre kursusnavn
        self.assertEqual(sch.get_course_name(), "Programmering")

        self.assertEqual(sch.get_course_id(), 342)
        sch.set_course_id(545) #Ændre KursusID
        self.assertEqual(sch.get_course_id(), 545)

        self.assertEqual(sch.get_course_room(), 1)
        sch.set_course_room(45) #Ændre Lokale
        self.assertEqual(sch.get_course_room(), 45)

        self.assertEqual(sch.get_teacher(), "dff199")


        self.assertEqual(sch.get_course_schedule(), '')
        sch.course_scheduel_change(datetime.strptime("10:00 07/04/2022", "%H:%M %d/%m/%Y"), "10:00") #Tilføjer dag. NB. "%Y-%m-%d %H:%M:%S"
        sch.course_scheduel_change(datetime.strptime("10:00 10/04/2022", "%H:%M %d/%m/%Y"), "10:00")
        sch.course_scheduel_change(datetime.strptime("10:00 10/05/2022", "%H:%M %d/%m/%Y"), "10:00")
        self.assertEqual(sch.get_course_schedule(), '2022-04-07 10:00:00 - 10:00\n 2022-04-10 10:00:00 - 10:00\n 2022-05-10 10:00:00 - 10:00')
        sch.course_scheduel_change('2022-04-07 10:00:00', '10:00')
        sch.course_scheduel_change(datetime.strptime("10:00 25/04/2022", "%H:%M %d/%m/%Y"), "10:00")
        self.assertEqual(sch.get_course_schedule(), '2022-04-10 10:00:00 - 10:00\n 2022-05-10 10:00:00 - 10:00\n 2022-04-25 10:00:00 - 10:00')
        self.assertEqual(sch.__str__(), "**********\n CourseName: Programmering\n CourseID: 545\n CourseTeacher: dff199\n CourseRoom: 45\n CourseSchedule: 2022-04-10 10:00:00 - 10:00, 2022-05-10 10:00:00 - 10:00, 2022-04-25 10:00:00 - 10:00")

if __name__ == '__main__':
    unittest.main(verbosity=10)