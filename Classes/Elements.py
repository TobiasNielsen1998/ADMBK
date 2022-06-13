"""
Inspired by cookbook
"""
from lxml import objectify
from Teacher import *
from Course import Course


class Elements:
    """
    class supporting coursestoxml
    """
    @staticmethod
    def create_teacher(teacher_obj: Teacher):
        """
        defines the teacher object
        """
        teacher = objectify.Element("info")
        teacher.navn = teacher_obj.get_name()
        teacher.brugerID = teacher_obj.get_user_id()
        teacher.cpr = teacher_obj.get_cpr_number()
        teacher.tlf = teacher_obj.get_phone()
        teacher.email = teacher_obj.get_email()
        return teacher

    @staticmethod
    def create_course(course_obj: Course):
        """
        defines the course object
        """
        course = objectify.Element("kursus")
        course.kursusID = course_obj.get_course_id()
        course.kursusnavn = course_obj.get_course_name()
        course.fakultet = course_obj.get_course_faculty()
        course.lokale = course_obj.get_course_room()
        course.skema = course_obj.get_course_schedule()
        return course