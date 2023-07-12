"""
data_loader.py

This file contains logic behind adding attendance entries into
sqlite database
"""

import csv
from attendance_system.models import Attendance
from django.db import IntegrityError


def csv_to_database():
    """
    This function will load data from attendance.csv file
    and add into sqlite database.
    """
    file_path = "media/csv/attendance.csv"
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            (
                seat_number,
                date,
                entrance_time,
            ) = row  # Adjust the assignment based on your CSV structure
            try:
                Attendance.objects.create(
                    seat_number=seat_number, date=date, entrance_time=entrance_time
                )
            except IntegrityError:
                pass
