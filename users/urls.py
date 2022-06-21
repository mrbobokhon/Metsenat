from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentsView.as_view()),
    path('students/<int:pk>', StudentsDetailView.as_view()),
    path('sponsors/', SponsorsView.as_view()),
    path('sponsors/<int:pk>', SponsorsDetailView.as_view()),
    path('app_form/', SponsorApplicationView.as_view()),
    path('university', UniversityView.as_view()),
    path('university/<int:pk>', UniversityDetailView.as_view),
] 