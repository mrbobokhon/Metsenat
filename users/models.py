from email.policy import default
from optparse import Values
from django.db import models
from django.dispatch import receiver
from django.forms import IntegerField
from datetime import date
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from rest_framework.exceptions import ValidationError


today = date.today()
# Create your models here.


# BaseModel
class BaseModel(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.CharField(max_length=250)
    # created_by = models.OneToOneField(
    #     User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


# University
class University(BaseModel):
    university_name = models.CharField("Universtitetning Nomi", max_length=250)

    class Meta:
        verbose_name = "Universitet"
        verbose_name_plural = "Universitet"

    def __str__(self):
        return self.university_name


# Sponsor
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


class Sponsor(BaseModel):
    person = models.IntegerField(
        "Shaxs turi",
        choices=PERSON
    )
    full_name = models.CharField("F.I.SH", max_length=250)
    number = models.CharField("Telefon Raqam", max_length=250)
    name_of_company = models.CharField("Firma/Kompaniya nomi", max_length=250)
    condition = models.IntegerField(
        "Holat",
        choices=CONDITIONS
    )
    budget = models.IntegerField(default=0)

    def value_to_string(self, obj):
        value = self.value_from_object(self.money)
        return self.get_prep_value(value)

    class Meta:
        verbose_name = "Homiylar"
        verbose_name_plural = "Homiylar"

    def __str__(self):
        return self.full_name


    # Students
MAJORS = [
    (1, "Bakalavr"),
    (2, "Magistratura"),
    (3, "Aspirantura"),
]


class Student(BaseModel):
    photo = models.ImageField("Rasim", upload_to=today)
    full_name = models.CharField("F.I.SH", max_length=250)
    number = models.IntegerField("Telefon Raqam")
    university = models.ForeignKey(
        University, verbose_name="Institut", on_delete=models.CASCADE)
    major = models.IntegerField(
        "Talim turi",
        choices=MAJORS
    )
    demand = models.IntegerField("Soralgan pull miqdori")
    paid_money = models.IntegerField("To'langan pull miqdori")

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"

    def __str__(self):
        return self.full_name


class StudentSponsor(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Talaba")
    sponsor = models.ForeignKey(
        Sponsor, verbose_name="Homiy", on_delete=models.CASCADE)
    money = models.IntegerField(verbose_name="Pull miqdori")

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

    if sponsor.budget >= instance.money and student.demand >  student.paid_money and student_reminder >= instance.money:
        sponsor.budget -= instance.money
        student.paid_money += instance.money
        student.save()
        sponsor.save()
    else:
        raise ValidationError(f"{instance.money} Bu summani Qosha olamaysiz")

