from django.shortcuts import get_object_or_404, render
from .models import Student, Attendance
from scripts import data_loader


def index(request):
    """
    Function to handle homepage of Web Application.
    """

    # Updating data in realtime
    data_loader.csv_to_database()

    # fetching data
    attendance_records = Attendance.objects.all()

    # context
    attendance_records = {
        "attendance_record": attendance_records,
    }

    return render(request, "home.html", attendance_records)


def student(request, seat_number):
    """
    Function to handle student information page.
    """

    # Fetching student data from database
    student_info = get_object_or_404(Student, seat_number=seat_number)

    # context
    context = {
        "student": student_info,
    }

    return render(request, "student.html", context)
