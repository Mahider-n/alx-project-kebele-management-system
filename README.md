 
# 🏢 Kebele Management System

A Django-based API for managing **residents and admins** at a Kebele level.
This system supports **user registration, authentication, and CRUD operations** using Django REST Framework and JWT.

---

## 🚀 Features

The Kebele Management System is designed with both **Resident (user-facing)** and **Admin (staff-facing)** features.

### ✅ Current Features (Implemented)

* 🔐 **JWT Authentication** (login & token refresh).
* 👥 **User CRUD** (register, view, update, delete).
* 🧑‍💼 **Role-based access**:

  * Residents can register and manage their own profiles.
  * Admins can view all users.
* 📸 **Profile picture upload** support.
* ⚡ Built with **Django ORM** (no raw SQL).

---

### 🧑‍🤝‍🧑 User-Facing Features (Resident Portal)

* **Service Information Hub**

  * Guides for applying for services like:

    * New/renewed IDs
    * Birth, marriage, and death certificates
  * Details on requirements, fees, and timelines

* **Online Registration**

  * Residents can apply for services by filling forms with personal details (name, address, contact info)
  * Upload necessary documents (e.g., ID photos, proofs)

* **Application Status Tracking**

  * Real-time updates (e.g., *Pending Review*, *In Process*, *Ready for Pickup*)

* **Notifications**

  * Alerts when documents are ready
  * Requests for missing/extra information

* **User Authentication**

  * Secure signup/login via email or phone number
  * Password reset functionality

* **Search & FAQ**

  * Searchable knowledge base for common questions

---

### 🧑‍💼 Admin-Facing Features (Kebele Dashboard)

* **Dashboard Overview**

  * Track metrics: number of users, pending applications, completed services

* **Application Management**

  * View/review/approve/reject applications
  * Add notes or request more details from residents

* **User Notification System**

  * Send bulk or individual notifications (e.g., *Your ID is ready for pickup*)

* **Reporting Tools**

  * Generate reports on service usage (daily/weekly stats, demographics)

* **Admin Authentication**

  * Role-based access (super admins for kebele heads, staff for processing)

---

### ⚙️ Functional Requirements

#### 1. Users (Residents) — CRUD

* **Create**: Register account (email, password, full name, phone, address, profile picture)
* **Read**: Get profile and list applications
* **Update**: Edit profile details
* **Delete**: (Optional) soft-delete account

#### 2. Admins — Pre-created Accounts

* Seeded via admin panel or migration
* Can manage any application (list, read, update, delete, assign officer)

#### 3. Applications — CRUD

* **Create**: Resident submits service application (type, fields, attachments)
* **Read**: Resident + admins can view details
* **Update**: Resident can edit *while Pending Review*; Admins can edit anytime
* **Delete**: Residents can withdraw; Admins can remove if needed

**Default status**: `Pending Review`
**Statuses**: `Pending Review`, `Ready for Pickup`, `Rejected`

#### 4. Dashboards

* Resident dashboard: list of applications + statuses
* Admin dashboard: filter applications by service, status, date

#### 5. Notifications (undecided)

* Notify residents on status changes (email/in-app)

#### 6. Service Information Pages

* Public endpoints listing available services, required documents, fees, timelines


---

## 🛠️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Auth**: djangorestframework-simplejwt
* **Database**: SQLite (dev) / PostgreSQL (prod-ready)
* **Image Handling**: Pillow

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/kebele-management-system.git
   cd kebele-management-system
   ```

2. Create & activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

---

## 🔑 API Endpoints

Base URL: `http://127.0.0.1:8000/api/v1/auth/`

### Auth

* `POST /register/` → Register new user
* `POST /login/` → Login & get JWT token
* `POST /token/refresh/` → Refresh token

### Users

* `GET /users/` → List all users (**admin only**)
* `GET /users/{id}/` → Get user by ID
* `PATCH /users/{id}/` → Update user partially
* `DELETE /users/{id}/` → Delete user

---

## 🧪 Testing with Postman

1. Register a user:

   ```json
   {
     "username": "name",
     "password": "mypassword",
     "email": "name@example.com",
     "full_name": "name name",
     "phone_number": "0911223344",
     "address": "Addis Ababa"
   }
   ```

2. Login to get JWT token:

   ```json
   {
     "username": "name",
     "password": "mypassword"
   }
   ```

   Response:

   ```json
   {
     "refresh": "xxxx",
     "access": "yyyy"
   }
   ```

3. Use the **access token** in Postman → Headers:

   ```
   Authorization: Bearer <access_token>
   ```

---

## 🛤️ Roadmap

* [ ] CRUD for Services (e.g., certificates, documents)
* [ ] Application model (residents apply for services)
* [ ] Admin approval/rejection workflow
* [ ] Unit tests for API endpoints

---


