"""
Inspired by cookbook
"""
from lxml import objectify
from Courses import Courses, Course

class XmlToCourses:
    """
    class to convert xmldata to course objects
    """
    def __init__(self, xml_filename : str):
        self.xml_filename = xml_filename

    def parseXML(self) -> Courses:
        """
        takes a xml file, and converts the data to objects
        """
        with open(self.xml_filename, "rb") as f:
            xml = f.read()

        root = objectify.fromstring(xml)

        # Return attributes in element node as a dictionary
        attrib = root.attrib

        courseList = Courses()

        # Loop over all courses in the xml file
        for course in root.getchildren():
            # create course object with the attributes and the list of students
            course_obj = Course(course.kursusID,course.kursusnavn,course.fakultet, course.lokale, "")
            course_obj.course_scheduel_change(course.skema, "")
            # add the course to the course list:

            courseList.append_course(course_obj)

        return courseList