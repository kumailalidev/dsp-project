from django.db import models


class Student(models.Model):
    """
    Student object model for storing student information
    """

    seat_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    program = models.CharField(max_length=50)
    enrollment_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to="students_data/images", null=True)

    def __str__(self):
        return self.seat_number


class Attendance(models.Model):
    """
    Attendance object model for attendance entry.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    entrance_time = models.TimeField()

    class Meta:
        unique_together = ("student", "date")

    def __str__(self):
        return str(self.date) + ": " + self.student.seat_number
