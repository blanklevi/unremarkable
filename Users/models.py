from django.db import models
import re


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        FN_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not FN_REGEX.match(postData['first_name']):
            errors['first_name'] = "Only letters can be used for First Name"
        LN_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not LN_REGEX.match(postData['last_name']):
            errors['last_name'] = "Only letters can be used for Last Name"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email Address"
        PW_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        if not PW_REGEX.match(postData['password']):
            errors['password'] = "Invalid characters for password"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long!"
        if len(postData['email']) < 2:
            errors['email'] = "Email address is required!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long!"
        return errors

    def log_in_validator(self, postData):
        errors = {}
        if len(postData['log_email']) < 2:
            errors['log_email'] = "Email address is required!"
        if len(postData['log_pw']) < 8:
            errors['log_pw'] = "Password must be at least 8 characters long!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()