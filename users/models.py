from email.mime import image
import numbers
from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from datetime import date

today = date.today()

# Create your models here.


# Application form
PERSON = [
    ("yuridik", "Yuridik"),
    ("jismoniy", "Jismoniy"),
]


class SponsorApplication(models.Model):
    person = models.CharField(
        max_length=20,
        choices=PERSON,
    )
    full_name = models.CharField(max_length=100)
    number = models.IntegerField()
    money = IntegerField()
    name_of_company = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ariza Formasi"
        verbose_name_plural = "Ariza Formasi"

    def __str__(self):
        return self.full_name


# Sponsors
CONDITIONS = [
    ("yangi", "Yangi"),
    ("tasdiqlangan", "Tasdiqlamgan"),
    ("moderatsiyada", "Moderatsiyada"),
    ("bekor qilingan", "Bekor Qilingan"),
]

class UniversityModel(models.Model):
    name_of_university = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitet"

    def __str__(self):
        return self.name_of_university

class Sponsor(models.Model):
    shaxs = models.CharField(
        max_length=20,
        choices=PERSON
    )
    full_name = models.CharField(verbose_name="Toliq isim", max_length=100)
    number = models.IntegerField()
    money = IntegerField()
    name_of_company = models.CharField(max_length=100)
    condition = models.CharField(
        max_length=20,
        choices=CONDITIONS
    )

    class Meta:
        verbose_name = "Homiylar"
        verbose_name_plural = "Homiylar"

    def __str__(self):
        return self.full_name


# Students
MAJORS = [
    ("bakalavr", "Bakalavr"),
    ("magistratura", "Magistratura"),
    ("aspirantura", "Aspirantura"),
]



class Student(models.Model):
    photo = models.ImageField(upload_to=today)
    full_name = models.CharField(max_length=100)
    number = models.IntegerField()
    university = models.ForeignKey(UniversityModel, on_delete= models.CASCADE)
    major = models.CharField(
        max_length=50,
        choices=MAJORS
    )
    demand = models.IntegerField()
    paid_money = models.IntegerField()
    sponsors = models.ManyToManyField(Sponsor, verbose_name="Sponsors of Students")

    class Meta:
        verbose_name = "O'quvchilar"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return self.full_name
