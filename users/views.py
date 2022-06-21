from urllib import response
from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import generics


# Create your views here.
class StudentsView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentsDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SponsorsView(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorsDetailView(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorApplicationView(generics.CreateAPIView):
    queryset = SponsorApplication.objects.all()
    serializer_class = SponsorApplicationSerializer


class UniversityView(generics.ListAPIView):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerialiser


class UniversityDetailView(generics.RetrieveAPIView):
    queryset = UniversityModel
    serializer_class = UniversitySerialiser