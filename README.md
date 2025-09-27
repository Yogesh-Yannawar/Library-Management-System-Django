# 📚 Library Management System

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.x-green)](https://www.djangoproject.com/)

A **Django-based web application** to manage a library system. Admins can manage books and students, issue and return books, and track fines. Students can register, view issued books, and check due dates.

---

## 🛠 Features

### Admin
- Add, update, and delete books.
- Add, update, and delete student profiles.
- Issue and manage books.
- Track overdue fines.
- Search and filter books and students.
- Admin dashboard with statistics and quick actions.

### Student
- Register and login.
- View and edit profile.
- Check issued books and return dates.
- Request book issues.
- Dashboard showing current issued books and status.

### Common
- Responsive design using **Bootstrap 5**.
- Alerts for success, error, and notifications.
- Profile image upload and display.
- Pagination and search for lists.

---

## 💻 Installation

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/library-management-system.git
cd library-management-system
```
2. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create Super User
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```
5. Open in browser:
```bash
http://127.0.0.1:8000/
```
---
## 📸 Screenshots
