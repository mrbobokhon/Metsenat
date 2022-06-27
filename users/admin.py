from . import models as model
from django.contrib import admin
from .models import *

# Register your models here.

# @register(StudentModel)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','number','university','major','demand','paid_money')

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['full_name','number','name_of_company','budget', 'paid_money',]

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['university_name',]

@admin.register(StudentSponsor)
class StudentSponsotAdmin(admin.ModelAdmin):
    list_display = ['student', 'sponsor','money',]
