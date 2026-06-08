from django.db import models
from django.conf import settings

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"
        COMPLETED = "COMPLETED", "Completed"

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
        limit_choices_to={"role": "PATIENT"}
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_appointments",
        limit_choices_to={"role": "DOCTOR"}
    )
    date_time = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appt: {self.patient.username} -> {self.doctor.username} ({self.date_time.strftime('%Y-%m-%d %H:%M')})"