from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentsView.as_view()),
    path('student/<int:pk>', StudentsDetailView.as_view()),
    path('student-delete/<int:pk>', StudentDeleteView.as_view()),
    path('student-create/', StudentCreateView.as_view()),
    # 
    path('sponsor/', SponsorsView.as_view()),
    path('sponsor/<int:pk>', SponsorsDetailView.as_view()),
    path('sponsor-delete/<int:pk>', SponsorDeleteView.as_view()),
    path('sponsor-create/', SponsorCreateView.as_view()),
    # 
    path('university/', UniversityView.as_view()),
    path('university/<int:pk>', UniversityDetailView.as_view()),
    path('university-delete', UniversityDeleteView.as_view()),
    path('university-create/', UniversityCreateView.as_view),
] 