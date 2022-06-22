from urllib import response
from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import generics


# Create your views here.

# Students
class StudentsView(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentsDetailView(generics.RetrieveAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteView(generics.DestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


# Sponsors
class SponsorsView(generics.ListAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer


class SponsorsDetailView(generics.RetrieveAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer


class SponsorDeleteView(generics.DestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializer


class SponsorCreateView(generics.CreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorApplicationSerializer

# SponsorApplication
class SponsorApplicationCreateView(generics.CreateAPIView):
    queryset = SponsorApplicationModel.objects.all()
    serializer_class = SponsorApplicationSerializer
    print(SponsorApplicationModel.objects.all().count())

# University
class UniversityView(generics.ListAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer


class UniversityCreateView(generics.CreateAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer

class UniversityDeleteView(generics.DestroyAPIView):
    queryset = UniversityModel
    serializer_class  =UniversitySerializer