from email.mime import image
import numbers
from django.db import models
from django.forms import IntegerField
from datetime import date

today = date.today()

# Create your models here.


# Application form
SHAXS = [
    ("yuridik", "Yuridik"),
    ("jismoniy", "Jismoniy"),
]

class Applications_form(models.Model):
    shaxs = models.CharField(
        max_length=20,
        choices = SHAXS
    )
    full_name = models.CharField(max_length=100)
    number = models.IntegerField()
    money = IntegerField()
    name_of_company = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


# Sponsors
CONDITIONS = [
    ("yangi", "Yangi"),
    ("tasdiqlangan", "Tasdiqlamgan"),
    ("moderatsiyada", "Moderatsiyada"),
    ("bekor qilingan", "Bekor Qilingan"),
]

class Sponsor(models.Model):
    shaxs = models.CharField(
    max_length=20,
    choices = SHAXS
    )
    full_name = models.CharField(max_length=100)
    number = models.IntegerField()
    money = IntegerField()
    name_of_company = models.CharField(max_length=100)
    condition = models.CharField(
        max_length = 20,
        choices = CONDITIONS
    )

    def __str__(self):
        return self.full_name


# Students
MAJORS = [
    ("bakalavr","Bakalavr"),
    ("magistratura","Magistratura"),
    ("aspirantura","Aspirantura"),
]
UNIVERSITIES = [
    ("O’zbekiston milliy universiteti","O’zbekiston milliy universiteti"),
    ("Toshkent davlat texnika universiteti","Toshkent davlat texnika universiteti"),
    ("Toshkent davlat iqtisodiyot universiteti","Toshkent davlat iqtisodiyot universiteti"),
    ("O’zbekiston davlat jahon tillari universiteti","O’zbekiston davlat jahon tillari universiteti"),
    ("Toshkent davlat sharqshunoslik instituti","Toshkent davlat sharqshunoslik instituti"),
]
class Student(models.Model):
    photo = models.ImageField(upload_to = today)
    full_name = models.CharField(max_length=100)
    number = models.IntegerField()
    university = models.CharField(
        max_length=150,
        choices = UNIVERSITIES
        )
    major = models.CharField(
        max_length=50,
        choices = MAJORS
    )
    demand = models.IntegerField()
    paid_money = models.IntegerField()
    sponsors = models.ManyToManyField(Sponsor)

    def __str__(self):
        return self.full_name


