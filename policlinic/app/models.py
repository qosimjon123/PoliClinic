from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role_name


class Users(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class RoleDoctor(models.Model):
    role_doctor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_doctor_name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    role_doctor = models.ForeignKey(RoleDoctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role_doctor}"


class Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Запись на {self.date} {self.time} к {self.doctor}"


class MedicalReport(models.Model):
    record = models.ForeignKey(Records, on_delete=models.CASCADE)
    report_details = models.TextField()

    def __str__(self):
        return f"Справка для {self.record.first_name} {self.record.last_name} от {self.record.doctor}"
