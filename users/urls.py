from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentsView.as_view()),
    path('sponsors/', SponsorsView.as_view()),
    path('app_form/', ApplicationFormView.as_view()),
] 