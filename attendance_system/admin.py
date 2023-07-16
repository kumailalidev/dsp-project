from django.contrib import admin
from .models import Attendance, Student

admin.site.register(Student)
admin.site.register(Attendance)
