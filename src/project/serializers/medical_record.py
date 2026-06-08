from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import MedicalRecord

User = get_user_model()

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source="patient.username", read_only=True)
    doctor_username = serializers.CharField(source="doctor.username", read_only=True)

    class Meta:
        model = MedicalRecord
        fields = [
            "id",
            "patient",
            "patient_username",
            "doctor",
            "doctor_username",
            "prescription",
            "created_at",
            "complaints",
            "history_of_disease",
            "history_of_life",
            "preliminary_diagnosis",
            "recommendations",
            "diagnostic_referrals"
        ]
        read_only_fields = ["doctor", "created_at"]

    def validate_patient(self, value):
        if value.role != User.Role.PATIENT:
            raise serializers.ValidationError("Medical records can only be created for patients.")
        return value