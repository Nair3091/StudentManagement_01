# StudentManagement/urls.py
from django.contrib import admin
from django.urls import path, include
from students import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', student_views.students_list, name='students_list'),  # Set student list as the default page
]
