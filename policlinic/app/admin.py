from django.contrib import admin
from .models import Role, Users, RoleDoctor, Doctor, Records, MedicalReport

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'description']

@admin.register(RoleDoctor)
class RoleDoctorAdmin(admin.ModelAdmin):
    list_display = ['role_doctor_name']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'role_doctor']

@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'doctor', 'date', 'time']

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ['record', 'report_details']
