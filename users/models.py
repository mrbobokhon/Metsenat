from django.db import models
from django.dispatch import receiver
from django.forms import IntegerField
from datetime import date
from rest_framework.exceptions import ValidationError
from users.signals import *
from django.db.models.signals import pre_save, post_save, pre_delete


today = date.today()
# Create your models here.


# BaseModel
class BaseModel(models.Model):
    """This is a BaseModel"""
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.CharField(max_length=250)
    # created_by = models.OneToOneField(
    #     User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


# University
class University(BaseModel):
    """This is University info"""
    university_name = models.CharField(verbose_name="Universtitetning Nomi",
                                       max_length=250
                                       )

    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitetlar"

    def __str__(self):
        return self.university_name


# Sponsor
class Sponsor(BaseModel):
    """Thi is Sponsor info"""

    PERSON = [
        (1, "Yuridik"),
        (2, "Jismoniy"),
    ]
    CONDITIONS = [
        (1, "Yangi"),
        (2, "Tasdiqlamgan"),
        (3, "Moderatsiyada"),
        (4, "Bekor Qilingan"),
    ]

    person = models.IntegerField(verbose_name="Shaxs turi", choices=PERSON)
    full_name = models.CharField(verbose_name="F.I.SH", max_length=250)
    number = models.CharField(verbose_name="Telefon Raqam", max_length=250)
    name_of_company = models.CharField(verbose_name="Firma/Kompaniya nomi",
                                       max_length=250
                                       )
    condition = models.IntegerField("Holat", choices=CONDITIONS)
    budget = models.IntegerField(default=0)
    paid_money = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Homiy"
        verbose_name_plural = "Homiylar"

    def __str__(self):
        return self.full_name

    # Students


class Student(BaseModel):
    """This is Students info"""
    MAJORS = [
        (1, "Bakalavr"),
        (2, "Magistratura"),
        (3, "Aspirantura"),
    ]

    photo = models.ImageField(verbose_name="Rasim", upload_to=today)
    full_name = models.CharField(verbose_name="F.I.SH", max_length=250)
    number = models.IntegerField(verbose_name="Telefon Raqam")
    university = models.ForeignKey(University, verbose_name="Institut",
                                   on_delete=models.CASCADE
                                   )
    major = models.IntegerField(verbose_name="Talim turi", choices=MAJORS)
    demand = models.IntegerField(verbose_name="Soralgan pull miqdori")
    paid_money = models.IntegerField(verbose_name="To'langan pull miqdori")

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

    def __str__(self):
        return self.full_name


class StudentSponsor(models.Model):
    """Thi is a Student and Sponsor connected model with ForeignKey"""
    student = models.ForeignKey("users.Student", on_delete=models.CASCADE,
                                                                verbose_name="Talaba")
    sponsor = models.ForeignKey("users.Sponsor", verbose_name="Homiy",
                                on_delete=models.CASCADE)
    money = models.IntegerField(verbose_name="To'langan Pull miqdori")

    class Meta:
        verbose_name = "Talaba vs Homiy"
        verbose_name_plural = "Talaba va Homiylar"

    def __str__(self):
        return f"{self.student}  {self.sponsor}"


@receiver(pre_save, sender=StudentSponsor)
def check_budget(sender, instance, **kwargs):
    """"This pre_save Signal method checks the budget also adds  money or minuses"""
    student = Student.objects.get(id=instance.student.id)
    sponsor = Sponsor.objects.get(id=instance.sponsor.id)
    student_reminder = student.demand - student.paid_money

    if (sponsor.budget >= instance.money and
        student.demand > student.paid_money and
            student_reminder >= instance.money):

        sponsor.budget -= instance.money
        sponsor.paid_money += instance.money
        student.paid_money += instance.money
        student.save()
        sponsor.save()
    else:
        raise ValidationError(f"{instance.money} Bu summani Qosha olamaysiz")


@receiver(pre_delete, sender=StudentSponsor)
def delete_budeget(sender, instance, **kyargs):
    """"This Signal function deletes paid_money in both Student and Sponsor"""
    student = Student.objects.get(id=instance.student.id)
    sponsor = Sponsor.objects.get(id=instance.sponsor.id)

    student.paid_money -= instance.money
    sponsor.paid_money -= instance.money
    sponsor.budget += instance.money

    sponsor.save()
    student.save()
