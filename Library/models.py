from django.db import models
from django.contrib.auth.models import User
from datetime import datetime ,timedelta,date
# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.PositiveIntegerField()
    category=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} +[{self.isbn}]'

class Student(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    classroom=models.CharField(max_length=10)
    branch=models.CharField(max_length=30)
    roll_no=models.CharField(max_length=3,blank=True)
    phone =models.CharField(max_length=10,blank=True)
    image = models.ImageField(upload_to='image/',blank=True)

    def __str__(self):
        return f'{self.user} [{self.branch}] [{self.classroom}] [{self.roll_no}]'

def expiry():
    return date.today() + timedelta(days=14)

class IssuedBook(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE,null=True,blank=True)
    issued_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(default=expiry)

    def is_expired(self):
        return date.today() > self.expiry_date

    def fine_amount(self):
        if self.is_expired():
            overdue_days = (date.today() - self.expiry_date).days
            return overdue_days * 5   # ₹5 per day fine
        return 0

    def __str__(self):
        return f"{self.student} - {self.book}"


