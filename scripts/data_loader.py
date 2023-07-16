"""
data_loader.py

This file contains logic behind adding attendance entries into
sqlite database
"""

import csv
from attendance_system.models import Attendance, Student
from django.db import IntegrityError


def csv_to_database():
    """
    This function will load data from attendance.csv file
    and add into sqlite database.
    """
    file_path = "media/csv/attendance.csv"
    with open(file_path, "r") as file:
        student = Student()
        reader = csv.reader(file)
        for row in reader:
            try:
                # Getting data from CSV file
                (
                    seat_number,
                    date,
                    entrance_time,
                ) = row
                # Getting student object instance
                student = Student.objects.get(seat_number=seat_number)

                # Creating attendance object if student exists in database
                Attendance.objects.create(
                    student=student, date=date, entrance_time=entrance_time
                )

            except Student.DoesNotExist:
                print("[ERROR]: Failed to load student data.")

            except IntegrityError:
                print(f"[INFO]: Attendance record of {student.full_name} already exits")
            except ValueError:
                print(
                    "[ERROR]: Please check your CSV file, it may be empty or contains bad data"
                )
            except Exception as e:
                print(e.__class__.__name__)
