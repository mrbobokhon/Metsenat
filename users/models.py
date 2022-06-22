from django.db import models
from django.forms import IntegerField
from datetime import date

today = date.today()
# Create your models here.


# BaseModel
class BaseModel(models.Model):

    class Meta:
        abstract = True


# Application form
PERSON = [
    ("yuridik", "Yuridik"),
    ("jismoniy", "Jismoniy"),
]


class SponsorApplicationModel(BaseModel):
    person = models.CharField(
        "Shaxs",
        max_length=20,
        choices=PERSON,
    )
    full_name = models.CharField("F.I.SH",max_length=100)
    number = models.CharField("Telefon raqam",max_length=50)
    money = IntegerField()
    name_of_company = models.CharField("Firma/Kompaniya nomi",max_length=100)

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


class UniversityModel(BaseModel):
    name_of_university = models.CharField("Universtitetning Nomi",max_length=250)

    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitet"

    def __str__(self):
        return self.name_of_university


class SponsorModel(BaseModel):
    person = models.CharField(
        "Shaxs",
        max_length=20,
        choices=PERSON
    )
    full_name = models.CharField("F.I.SH",max_length=100)
    number = models.CharField("Telefon Raqam",max_length=50)
    money = IntegerField()
    name_of_company = models.CharField("Firma/Kompaniya nomi",max_length=100)
    condition = models.CharField(
        "Holat",
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

class StudentModel(BaseModel):
    photo = models.ImageField("Rasim",upload_to=today)
    full_name = models.CharField("F.I.SH",max_length=100)
    number = models.IntegerField("Telefon Raqam")
    university = models.ForeignKey(UniversityModel, verbose_name="Institut", on_delete=models.CASCADE)
    major = models.CharField(
        "Yo'nalish",
        max_length=50,
        choices=MAJORS
    )
    demand = models.IntegerField("Soralgan pull miqdori")
    paid_money = models.IntegerField("To'langan pull miqdori")
    sponsors = models.ManyToManyField(SponsorModel, verbose_name="Homiy")

    class Meta:
        verbose_name = "O'quvchilar"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return self.full_name
