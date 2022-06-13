"""
Inspired by cookbook
"""
from lxml import etree, objectify
from io import BytesIO
from Courses import Courses, Course
from Elements import Elements
from Teacher import Teacher

class CoursesToXml:
    """
    class to make xmldata of course + schedule + teacher
    """
    def __init__(self, courses: Courses, teachers :Teacher):
        self.courses = courses
        self.teachers = teachers

    def write_file(self):
        """
        writes xml file
        """
        root = etree.Element("kurser")
        for course in self.courses:
            obj_course = Course(course[0],course[1],course[2],course[3],course[4])
            obj_course.course_scheduel_change(course[5], "")
            course_element = Elements.create_course(obj_course)
            root.append(course_element)

            teachers =  objectify.SubElement(course_element,"underviser")
            for i in self.teachers:
                if obj_course.get_teacher() == i.get_user_id():
                    teacher_element = Elements.create_teacher(i)
                    teachers.append(teacher_element)

        # Do some cleanup
        # remove lxml annotation
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        # create the xml string
        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        # Write the xml string to a file
        try:
            with open("XML/courses.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass