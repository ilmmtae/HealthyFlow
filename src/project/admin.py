from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MedicalRecord, Appointment


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ("Medical Info", {"fields": ("role", "phone_number", "medical_id")}),
    )
    list_display = ["username", "email", "role", "is_staff"]


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "patient", "doctor", "preliminary_diagnosis", "created_at"]
    search_fields = ["patient__username", "doctor__username", "preliminary_diagnosis"]
    list_filter = ["created_at"]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "patient", "doctor", "date_time", "status"]
    list_filter = ["status", "date_time", "doctor"]
