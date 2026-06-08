from django.db import models
from django.conf import settings


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="medical_records",
        limit_choices_to={"role": "PATIENT"}
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_records",
        limit_choices_to={"role": "DOCTOR"}
    )


    complaints = models.TextField(blank=True, null=True, help_text="Current symptoms and complaints")
    history_of_disease = models.TextField(blank=True, null=True, help_text="Anamnesis morbi (how long it lasts, previous treatments)")
    history_of_life = models.TextField(blank=True, null=True, help_text="Anamnesis vitae (allergies, chronic diseases)")

    preliminary_diagnosis = models.CharField(max_length=255, blank=True, null=True, help_text="Preliminary or final diagnosis")

    prescription = models.TextField(blank=True, null=True, help_text="Medications prescribed by the doctor")
    recommendations = models.TextField(blank=True, null=True,  help_text="General recommendations (diet, lifestyle, etc.)")
    diagnostic_referrals = models.TextField(blank=True, null=True, help_text="Referrals for CT, MRI, X-Ray, blood tests, or other specialists")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sheet #{self.id} for {self.patient.username} by Dr. {self.doctor.username if self.doctor else 'Unknown'}"