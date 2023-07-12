from django.db import models


class Attendance(models.Model):
    """
    Student object model for attendance entry.
    """

    seat_number = models.CharField(max_length=20)
    date = models.DateField()
    entrance_time = models.TimeField()

    class Meta:
        unique_together = ("seat_number", "date")
