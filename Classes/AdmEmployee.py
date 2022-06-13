"""
Inspired by cookbook
"""
from stdnum.dk import cpr

class AdmEmployee:
    """
    AdmEmployee class holds attributes and methods for an AdmEmployee
    """
    def __init__(self, name: str, user_id: str, cpr_number: str, phone: str, email: str):
        self.__name = name
        self.__user_id = user_id
        try:
            self.__cpr_number = cpr_number
            cpr.get_birth_date(cpr.compact(self.__cpr_number))

        except TypeError as e:
            raise TypeError("bad cpr_number") from e
        self.__phone = phone
        self.__email = email

    def get_name(self):
        """
        Returns Administrative employee name
        """
        return self.__name

    def set_name(self, new_name):
        """
        Gives Administrative employee new name
        """
        self.__name = new_name

    def get_user_id(self):
        """
        Returns Administrative employee userid
        """
        return self.__user_id

    def set_user_id(self, new_user_id):
        """
        Gives Administrative employee new userid
        """
        self.__user_id = new_user_id

    def get_cpr_number(self):
        """
        Returns Administrative employee cprnumber
        """
        return cpr.compact(self.__cpr_number)

    def set_cpr_number(self, new_cpr):
        """
        Gives Administrative employee new cprnumber
        """
        self.__cpr_number = new_cpr

    def get_phone(self):
        """
        Returns Administrative employee phonenumber
        """
        return self.__phone

    def set_phone(self, new_phone):
        """
        Gives Administrative employee new phonenumber
        """
        self.__phone = new_phone

    def get_email(self):
        """
        Returns Administrative employee email
        """
        return self.__email

    def set_email(self, new_email):
        """
        Gives Administrative employee new email
        """
        self.__email = new_email


    def __str__(self):
        return f"*"*10+f"\n Name: {self.__name}\n UserID: {self.__user_id}\n CPR: {cpr.is_valid(self.__cpr_number)}\n Phone: {self.__phone}\n Email: {self.__email}"