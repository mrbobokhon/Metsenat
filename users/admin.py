import imp
from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Student)
admin.site.register(Sponsor)
admin.site.register(SponsorApplication)
admin.site.register(UniversityModel)
