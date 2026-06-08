# Healthy Flow

Healthy Flow is a backend ecosystem designed for efficient interaction between patients, doctors, and medical clinics. The project automates appointment scheduling, medical record management, and role-based access control, eliminating paperwork routine and chaos in healthcare workflows.

## Tech Stack

* **Programming Language:** Python 3.12+
* **Framework:** Django REST Framework (DRF)
* **Database:** PostgreSQL
* **Authentication:** JWT
* **Package Manager:** uv
* **Containerization:** Docker
* **API Documentation:** Swagger / OpenAPI

## Features

* **User & Role Management:** Custom user model with strict role separation (Admin, Clinic, Doctor, Patient).
* **Authentication:** Secure endpoint access using JWT tokens with user roles embedded into the token payload.
* **Appointment System:** Full appointment lifecycle management (creation by patients or clinics, dynamic status updates like `CONFIRMED` / `CANCELED` by doctors).
* **Medical Records:** Patient medical history management with rigid data isolation (patients can only access their own records; doctors can only access records of their assigned patients).
* **Security:** UUID primary keys (`id`) across all database entities and custom `Permissions` classes returning `403 Forbidden` for unauthorized access.


## Getting Started (Docker)

To run this project locally, you will need Docker installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ilmmtae/HealthyFlow.git]
   cd HealthyFlow
