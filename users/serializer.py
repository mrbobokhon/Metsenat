from dataclasses import fields
from rest_framework import serializers
from .models import *


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'


class SponsorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorApplicationModel
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UniversityModel
        fields = '__all__'