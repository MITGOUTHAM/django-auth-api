# Django Authentication API

This project is a **Django REST Framework Authentication API** that provides user registration with OTP verification, login/logout with JWT stored in HttpOnly cookies, and Swagger API documentation with CSRF protection.

---

## 🚀 Features
- **Register** → `POST /api/register/`  
  Register with email & password, OTP sent to console.  
- **Verify OTP** → `POST /api/verify-otp/`  
  Verify OTP and activate the user.  
- **Login** → `POST /api/login/`  
  Login and set `auth_token` cookie (HttpOnly).  
- **User Details** → `GET /api/me/`  
  Get logged-in user details (id, email, is_active).  
- **Logout** → `POST /api/logout/`  
  Clears the authentication cookie.  
- **Swagger Docs** → `/swagger/`  
  Test APIs with auto-generated CSRF token.  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

### 2. Create a virtual environment
python -m venv venv

Activate it:
- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Start the server
python manage.py runserver

Open Swagger docs at 👉 http://127.0.0.1:8000/swagger/

---

## 🔐 Security
- Authentication uses **HttpOnly cookies** (no tokens in headers).
- CSRF protection enabled automatically in Swagger.
- In production, set these in settings.py:
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True

---

## 📌 Notes
- OTPs are printed in the **console** (no external email setup needed for testing).
- db.sqlite3 and venv/ are excluded via .gitignore.
- To create an admin user:
  python manage.py createsuperuser











