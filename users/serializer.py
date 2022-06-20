from dataclasses import fields
from rest_framework import serializers
from .models import *


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SponsorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorApplication
        fields = '__all__'
        