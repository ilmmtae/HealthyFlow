from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegisterView, UserMeView, MedicalRecordListCreateView, AppointmentListCreateView, \
    AppointmentUpdateView, PatientMedicalHistoryView, PatientAppointmentsListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("me/", UserMeView.as_view(), name="user-me"),
    path("records/", MedicalRecordListCreateView.as_view(), name="medical-record-list-create"),
    path("appointments/", AppointmentListCreateView.as_view(), name="appointment-list-create"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('appointments/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment-detail'),
    path('records/my-history/', PatientMedicalHistoryView.as_view(), name='patient-medical-history'),
    path('appointments/my-appointments/', PatientAppointmentsListView.as_view(), name='patient-appointments'),
]