from .views import *
from django.urls import path

urlpatterns = [
path('',apioverview,name='apioverview'),
path('university',UniversityList.as_view(),name='university'),
path('university/<int:id>',UniversityDetail.as_view(),name='university-detail'),
path('students',StudentsList.as_view(),name='students'),
path('students/<int:id>',StudentsDetail.as_view(),name='students-detail')
]