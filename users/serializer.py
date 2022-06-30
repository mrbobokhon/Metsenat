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


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'

class StudentSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSponsor
        fields = '__all__'