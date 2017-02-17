
from django.db import models
from datetime import date

class Login(models.Model):
    userName=models.CharField(max_legnth=100)
    email=models.EmailField(max_legnth=60)
    gender=models.
    dob=models.DateField(_("Date"), default=date.today)
    passwords=models.CharField(max_legnth=40)
