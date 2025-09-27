from django import forms
from .models import IssuedBook, Student, Book
from django.contrib.auth.models import User

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['student', 'book']   # only these two are filled by user

        labels = {
            'student': 'Select Student',
            'book': 'Select Book',
        }

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['classroom','branch','roll_no','phone','image']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

