"""
Inspired by cookbook
"""
from datetime import *
from Teacher import Teacher
from Schedules import Schedules

class Course:
    """
    Schedule class holds attributes and methods for a schedeule
    """
    def __init__(self, course_id: int, course_name: str, course_faculty: str, course_room: int, teacher: Teacher):
        course_days: list[date] = []
        id_ranges = [i for i in range(1,1000)]
        room_numbers = [i for i in range(1,99)]
        try:
            if course_name != "":
                self.__course_name = course_name
        except TypeError as e:
            raise TypeError("Bad CourseName") from e
        try:
            if course_id in id_ranges:
                self.__course_id = course_id
        except TypeError as e:
            raise TypeError("Bad CourseID") from e
        try:
            if course_room in room_numbers:
                self.__course_room = course_room
        except TypeError as e:
            raise TypeError("Bad CourseRoom") from e
        try:
            if isinstance(teacher, Teacher):
                self.teacher = teacher.get_user_id()
            else:
                self.teacher = teacher
        except TypeError as e:
            raise TypeError("Bad CourseTeacher") from e
        self.__course_faculty = course_faculty
        self.course_days: list[date] = course_days

    def get_course_name(self):
        """
        Returns course name
        """
        return self.__course_name

    def set_course_name(self, new_course_name):
        """
        Sets new course name
        """
        self.__course_name = new_course_name

    def get_course_id(self):
        """
        Returns course id
        """
        return self.__course_id

    def set_course_id(self, new_course_id):
        """
        Gives course a new id
        """
        self.__course_id = new_course_id
    
    def get_course_faculty(self):
        """
        Returns course faculty
        """
        return self.__course_faculty

    def set_course_faculty(self, new_course_faculty):
        """
        Gives course a new faculty
        """
        self.__course_faculty = new_course_faculty

    def get_course_room(self):
        """
        Returns course room
        """
        return self.__course_room

    def set_course_room(self, new_course_room):
        """
        Gives course a new room
        """
        self.__course_room = new_course_room

    def get_course_schedule(self):
        """
        Returns course schedule
        """
        return '\n '.join(h for h in self.course_days).strip("[").strip("] -").replace(",","\n")

    def course_scheduel_change(self, day, day_end):
        """
        Adds new schedule day
        """
        if str(day) + " - " + str(day_end) not in self.course_days:
            self.course_days.append(Schedules().add_course_days(day, day_end))
            
        elif str(day) + " - " + str(day_end) in self.course_days:
            self.course_days.remove(Schedules().remove_course_days(day, day_end))

    def set_teacher(self, new_teacher):
        """
        Gives course a new teacher
        """
        self.teacher = new_teacher.get_user_id()

    def get_teacher(self):
        """
        Returns course teacher
        """
        return self.teacher

    def __str__(self=None):
        output = ', '.join(h for h in self.course_days)
        return "*"*10+f"\n CourseName: {self.__course_name}\n CourseID: {self.__course_id}\n CourseTeacher: {self.teacher}\n CourseRoom: {self.__course_room}\n CourseSchedule: {output}"