from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
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
    path('university-delete/<int:pk>', UniversityDeleteView.as_view()),
    path('university-create/', UniversityCreateView.as_view),
    # 
    path('student-sponsor/',StudentSponsorView.as_view()),
    path('student-sponsor/<int:pk>',StudentSponsorDetailView.as_view()),
    path('student-sponsor-create/',StudentSponsorCreateView.as_view()),
    path('student-sponsor-delete/<int:pk>',StudentSponsorDeleteView.as_view()),
] 