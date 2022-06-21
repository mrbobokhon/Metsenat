from . import models as model
from django.contrib import admin
from .models import *

# Register your models here.

# @register(StudentModel)
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','number','university','major','demand','paid_money')

@admin.register(SponsorModel)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['full_name','number','name_of_company',]

@admin.register(SponsorApplicationModel)
class SponsorApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name','person','money','name_of_company',]

@admin.register(UniversityModel)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name_of_university',]
