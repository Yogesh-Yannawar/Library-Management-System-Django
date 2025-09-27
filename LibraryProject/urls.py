"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static 
from Library.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('add_book/',add_book,name='add_book'),
    path('view_books/',view_books,name='view_books'),
    path('update_book/<id>/',update_book,name='update_book'),
    path('delete_book/<id>/',delete_book,name='delete_book'),
    path('add_student/',add_student,name='add_student'),
    path('view_student/',all_view,name='view_student'),
    path('delete_student/<id>/',delete_student,name='delete_student'),
    path('update_student/<id>/',update_student,name='update_student'),

    path('issue_book/',issue_book,name='issue_book'),
    path('view_issued_book/',view_issued_book,name='view_issued_book'),
    path('delete_issued_book/<id>/',delete_issued_book,name='delete_ib'),

    path('profile/',profile,name='profile'),
    path('edit_profile/',update_profile,name='edit_profile'),

    path('admin_login/',admin_login,name='admin_login'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin_login/',admin_login,name='admin_login'),
    path('logout_page/',logout_page,name='logout_page'),
    path('logout/',logout_view,name='logout'),
    path('student_register/',student_register,name='register'),
    path('stud_login/',stud_login,name='stud_login'),
    path('dashboard/',stud_dashboard,name='dashboard'),
    path('library-admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('library-admin/logout/', admin_logout, name='admin_logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
