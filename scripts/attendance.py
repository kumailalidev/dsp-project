"""
attendance.py

This file contains logic behind marking attendance.
"""

# Import necessary packages
import datetime


def mark_attendance(seat_number):
    """
    This function will mark attendance of students. If
    attendance of student is already marked, it skips
    and marks attendance of new student.
    """
    with open("media/csv/attendance.csv", "r+") as csv_file:
        # Check for already marked attendance inside csv file
        attendance_list = csv_file.readlines()
        seat_numbers = []

        for attendance in attendance_list:
            entry = attendance.split(",")[0]
            seat_numbers.append(entry)

        # If entry is not present inside attendance file then mark attendance.
        if seat_number not in seat_numbers:
            current_datetime = datetime.datetime.now()
            f_date = current_datetime.date().isoformat()
            f_time = current_datetime.time().strftime("%H:%M:%S")

            csv_file.writelines(f"\n{seat_number},{f_date},{f_time}")
            print(f"ATTENDANCE MARKED: {seat_number}")
