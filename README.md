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

  ## Screen shots

<img width="1920" height="1080" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/fba21d5e-db80-4235-900a-421f4b2f9463" />
<img width="1920" height="1080" alt="Screenshot (98)" src="https://github.com/user-attachments/assets/fb8cf8ca-7f55-4ede-9352-94805a1c26c0" />
<img width="1920" height="1080" alt="Screenshot (99)" src="https://github.com/user-attachments/assets/25522dd8-6ae1-42d6-9076-2952b74fb22f" />
<img width="1920" height="1080" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/68eeff82-9913-4b35-9b77-853fd60fbbb8" />
<img width="1920" height="1080" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/d8cab041-d77a-4367-ba9a-e6faeffa700a" />
<img width="1920" height="1080" alt="Screenshot (102)" src="https://github.com/user-attachments/assets/03482628-b4ee-4f8e-af3b-1f9e8dcc8784" />
<img width="1920" height="1080" alt="Screenshot (103)" src="https://github.com/user-attachments/assets/c06caa24-1143-4716-8adb-866d0d55fe09" />
<img width="1920" height="1080" alt="Screenshot (104)" src="https://github.com/user-attachments/assets/d0b911e8-2a49-4672-95d5-e78911b94e7b" />
<img width="1920" height="1080" alt="Screenshot (105)" src="https://github.com/user-attachments/assets/e9a0def0-a10b-40b4-8e27-05b20d96004d" />
<img width="1920" height="1080" alt="Screenshot (106)" src="https://github.com/user-attachments/assets/205f0a39-d3c3-494a-bc41-8f36820cd25e" />
<img width="1920" height="1080" alt="Screenshot (107)" src="https://github.com/user-attachments/assets/59adeb4d-d975-4d24-9b76-451d5a597aeb" />
<img width="1920" height="1080" alt="Screenshot (108)" src="https://github.com/user-attachments/assets/e2040af1-35b0-4358-87e6-7780d89ab94b" />
<img width="1920" height="1080" alt="Screenshot (109)" src="https://github.com/user-attachments/assets/190714de-56b3-4796-a7dd-fe61339775a8" />
<img width="1920" height="1080" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/b389424f-747b-42c0-bbce-97763dd39ea6" />









