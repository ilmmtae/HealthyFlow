from rest_framework import status, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import MedicalRecord, Appointment
from .serializers import UserRegisterSerializer, UserMeSerializer, MedicalRecordSerializer, AppointmentSerializer
from .serializers.appointment import AppointmentStatusUpdateSerializer


# Create your views here.


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "user_id": user.id,
                    "username": user.username,
                    "role": user.role
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserMeSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicalRecordListCreateView(ListCreateAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "DOCTOR":
            return MedicalRecord.objects.all().order_by("-created_at")

        elif user.role == "PATIENT":
            return MedicalRecord.objects.filter(patient=user).order_by("-created_at")

        return MedicalRecord.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != "DOCTOR":
            raise PermissionDenied("Only doctors can create medical records.")

        serializer.save(doctor=self.request.user)


class AppointmentListCreateView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "PATIENT":
            return Appointment.objects.filter(patient=user).order_by("date_time")
        elif user.role == "DOCTOR":
            return Appointment.objects.filter(doctor=user).order_by("date_time")
        return Appointment.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role != "PATIENT":
            raise PermissionDenied("Only patients can book appointments.")
        serializer.save(patient=self.request.user)

class AppointmentUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentStatusUpdateSerializer
    permission_classes = [IsAuthenticated]

class PatientMedicalHistoryView(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicalRecord.objects.filter(patient=self.request.user)

class PatientAppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)