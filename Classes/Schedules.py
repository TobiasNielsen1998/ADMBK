from datetime import *
from urllib.request import Request
from Requests import Requests

class Schedules:
    """
    Schedule class holds attributes and methods for a schedeule
    """
    def __init__(self):
        request: str = ""
        self.request = request
    
    def schedule_requests(self, request: Request):
        """
        Attatches note to course
        """
        self.request = Requests().schedule_request(request)

    def add_course_days(self, new_day : datetime, new_day_end : time):
        """
        Adds new schedule day
        """
        return str(new_day) + " - " + str(new_day_end)
    
    def remove_course_days(self, old_day : datetime, old_day_end : date):
        """
        Removes current schedule day
        """
        return str(old_day) + " - " + str(old_day_end)
