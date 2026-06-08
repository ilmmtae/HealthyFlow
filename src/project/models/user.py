from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"
        CLINIC = "CLINIC", "Clinic"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT,
        verbose_name="Role"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Phone number"
    )
    medical_id = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Medical ID / Clinic License"
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"