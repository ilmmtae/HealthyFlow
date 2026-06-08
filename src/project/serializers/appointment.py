from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Appointment

User = get_user_model()

class AppointmentSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source="patient.username", read_only=True)
    doctor_username = serializers.CharField(source="doctor.username", read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "patient", "patient_username", "doctor", "doctor_username", "date_time", "reason", "status", "created_at"]
        read_only_fields = ["patient", "status", "created_at"]

    def validate_doctor(self, value):
        if value.role != User.Role.DOCTOR:
            raise serializers.ValidationError("Appointments can only be booked with doctors.")
        return value

class AppointmentStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['status']