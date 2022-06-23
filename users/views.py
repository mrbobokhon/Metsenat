from urllib import response
from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import generics


# Create your views here.

# Students
class StudentsView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentsDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Sponsors
class SponsorsView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorsDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDeleteView(generics.DestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorCreateView(generics.CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


# University
class UniversityView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityCreateView(generics.CreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class UniversityDetailView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDeleteView(generics.DestroyAPIView):
    queryset = University.objects.all()
    serializer_class  =UniversitySerializer


# StudentSponsor
class StudentSponsorView(generics.ListAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentSponsorDetailView(generics.RetrieveAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentSponsorCreateView(generics.CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer

class StudentSponsorDeleteView(generics.DestroyAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer