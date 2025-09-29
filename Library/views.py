from django.shortcuts import render,redirect
from .models import IssuedBook,Student,Book
from django.contrib.auth.models import User
from .forms import IssueBookForm,UserForm,StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='admin_login')
def add_book(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        isbn=request.POST.get('isbn')
        category=request.POST.get('category')
        if not isbn.isdigit() or len(isbn) > 9:
            messages.error(request, 'ISBN number must be numeric and maximum 9 digits.')
        Book.objects.create(name=name,author=author,isbn=isbn,category=category)
        alert=True
        return render(request,'add_book.html',{'alert':alert})       
    return render(request,'add_book.html')

@login_required(login_url='admin_login')
def view_books(request):
    books=Book.objects.all()
    return render(request,'view_books.html',{'books':books})

@login_required(login_url='admin_login')
def update_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        isbn=request.POST.get('isbn')
        category=request.POST.get('category')
        book.name=name
        book.author=author
        book.isbn=isbn
        book.category=category
        book.save()
        return redirect ('view_books')
    return render(request,'update_book.html',{'book':book})

@login_required(login_url='admin_login')
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('view_books')

@login_required(login_url='admin_login')
def add_student(request):
    if request.method=='POST':
        user_id=request.POST.get('user')
        user=User.objects.get(id=user_id)
        classroom=request.POST.get('classroom')
        branch=request.POST.get('branch')
        roll_no=request.POST.get('roll_no')
        phone =request.POST.get('phone')
        image = request.FILES.get('image')
        Student.objects.create(
            user=user,
            classroom=classroom,
            branch=branch,
            roll_no=roll_no,
            phone=phone,image=image)
        return redirect('view_student')
    users=User.objects.all()
    return render(request,'add_student.html',{'users':users})

@login_required(login_url='admin_login')
def all_view(request):
    students=Student.objects.all()
    return render(request,'view_student.html',{'students':students})

@login_required(login_url='admin_login')
def delete_student(request,id):
    stud=Student.objects.get(id=id)
    stud.delete()
    return redirect('view_student')

@login_required(login_url='admin_login')
def update_student(request,id):
    stud=Student.objects.get(id=id)
    if request.method=='POST':
        stud.user_id=request.POST.get('user')
        stud.classroom=request.POST.get('classroom')
        stud.branch=request.POST.get('branch')
        stud.roll_no=request.POST.get('roll_no')
        stud.phone =request.POST.get('phone')
        stud.image=request.FILES.get('image')
        stud.save()
        return redirect('view_student')
    users=User.objects.all()
    return render(request,'update_student.html',context={'stud':stud,'users':users})

@login_required(login_url='admin_login')
def issue_book(request):
    if request.method=='POST':
        form=IssueBookForm(request.POST)
        if form.is_valid():
            form.save()
            alert=True
            return render(request,'issue_book.html',context={'form':IssueBookForm(),'alert':alert})
    form=IssueBookForm()
    return render(request,'issue_book.html',context={'form':form})

@login_required(login_url='admin_login')
def view_issued_book(request):
    issued_books = IssuedBook.objects.select_related('student', 'book').all().order_by('-issued_date')

    details = []
    for ib in issued_books:
        details.append({
            'student_name': ib.student.user.get_full_name() if ib.student else "N/A",
            'student_id': ib.student.id if ib.student else "N/A",
            'book_name': ib.book.name if ib.book else "N/A",
            'isbn': ib.book.isbn if ib.book else "N/A",
            'issued_date': ib.issued_date,
            'expiry_date': ib.expiry_date,
            'fine': ib.fine_amount(),
            'id': ib.id,  # for delete link
        })

    paginator = Paginator(details, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_issued_book.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_issued_book(request,id):
    ib=IssuedBook.objects.get(id=id)
    ib.delete()
    return redirect('view_issued_book')
    
@login_required(login_url='stud_login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='stud_login')
def update_profile(request):
    student=Student.objects.get(user=request.user)
    if request.method=='POST':
        student.roll_no=request.POST.get('roll_no')
        student.classroom=request.POST.get('classroom')
        student.branch=request.POST.get('branch')
        student.phone=request.POST.get('phone')
        student.user.save()
        student.save()
        alert=True
        return render(request,'edit_profile.html',{'alert':alert})
    return render(request,'edit_profile.html')


def admin_login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            if user.is_superuser and user.is_staff:
                login(request,user)
                return redirect('admin_dashboard')
            else:
                messages.error(request,'You are not authorized as Admin.')
        else:
            messages.error(request,'Invalid username or password.')
    return render(request,'admin_login.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('admin_login')
    return render(request, 'admin_dashboard.html')

@login_required(login_url='admin_login')
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('admin_login')

@login_required
def logout_view(request):
    logout(request)
    return redirect('logout_page')


def logout_page(request):
    return render(request,'logout_view.html')

def student_register(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)
        student_form=StudentForm(request.POST,request.FILES)

        if user_form.is_valid() and student_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            student=student_form.save(commit=False)
            student.user=user
            student.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('stud_login')
        else:
            messages.error(request,'Please enter correct Value')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request,'student_register.html',{'user_form':user_form,'student_form':student_form})

def stud_login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        messages.error(request,'Invalid Username or Password')
    return render(request,'stud_login.html')

@login_required(login_url='stud_login')
def stud_dashboard(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        student = None

    issued_books = IssuedBook.objects.filter(student=student) if student else []

    context = {
        'student': student,
        'issued_books': issued_books,
        'today': date.today(),   # ✅ Add this
    }
    return render(request, 'stud_dashboard.html', context)

def view_books(request):
    query = request.GET.get('q', '')  # get search input
    books_list = Book.objects.all().order_by('name')

    if query:
        books_list = books_list.filter(
            Q(name__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query) |
            Q(category__icontains=query)
        )

    paginator = Paginator(books_list, 5)  # optional, 5 per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_books.html', {'page_obj': page_obj, 'query': query})


def all_view(request):
    query = request.GET.get('q', '')  # get search input from GET request
    students_list = Student.objects.all().order_by('user__username')
    if query:
        students_list = students_list.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(branch__icontains=query)
        )
    paginator = Paginator(students_list, 4)  # 4 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_student.html', {'page_obj': page_obj, 'query': query})
