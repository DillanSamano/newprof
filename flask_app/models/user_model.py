import re 
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class User:
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.comment = data['comment']



@staticmethod
def user_validator(user):
        is_valid = True 
        if len(user['first_name']) < 6:
            flash("your name is not long enough!")
            is_valid = False

        if len(user['last_name']) < 4:
            flash("your last name is not long enough")
            is_valid = False
            

        if len(user['email']) < 4:
            flash("your username is not long enough")
            is_valid = False

        if len(user['exampleFormControlTextarea1'])< 10:
            flash("your email invalid!")
            is_valid = False


        return is_valid