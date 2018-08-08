from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Validate user registration
class Manager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
    # errors["name"] = "First name should be at least 2 characters"
            errors.append('first name must be greater than two characters')
        if len(postData['last_name']) < 2:
    # errors["desc"] = "Last name should be at least 2 characters"
            errors.append('Last name cant be less than two characters')
        elif not EMAIL_REGEX.match(postData['register_email']):
            errors.append('invalid email')
    # PASSWORD VALIDATOR (GREATER THAN 2)
        elif len(postData['register_password']) < 2:
            errors.append('provide a stronger password') 
    # CONFIRM PASSWORDS
        if postData['confirm_password'] != postData['register_password']:
            errors.append('passwords dont match!')
        return errors

    def login_validator(self, postData):
        errors = []
        user = users.objects.get(email = postData['login_email'])
        if postData['login_email'] != user.email or postData['login_password'] != user.password:
            errors.append('email/password are invalid')

        return errors



class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()
