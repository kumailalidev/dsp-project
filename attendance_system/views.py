from django.shortcuts import render
from .models import Attendance
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

    return render(request, "attendance_system/index.html", attendance_records)
