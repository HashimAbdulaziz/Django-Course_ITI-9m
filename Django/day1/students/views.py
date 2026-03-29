from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages


from .models import Student, Feedback, Grade, Subject


def home(request):
   return render(request, "home.html")


@login_required
def student_page(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      age = request.POST.get('age')
      email = request.POST.get('email')
      image = request.FILES.get('image')

      Student.objects.create(name=name, age=age, email=email, image=image)
      return redirect('student_page')
   
   students = Student.objects.all()
   return render(request, 'students.html', {'students': students})


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('student_page')


def contact_us(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        Feedback.objects.create(email=email, message=message)
        return redirect('home')
        
    return render(request, 'contact.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def subject_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Subject.objects.create(name=name)
        return redirect('subjects')
        
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})


@login_required
def grade_page(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        grade_value = request.POST.get('grade')
        
        student_obj = Student.objects.get(id=student_id)
        subject_obj = Subject.objects.get(id=subject_id)
        
        Grade.objects.update_or_create(
            student=student_obj, 
            subject=subject_obj,
            defaults={'score': grade_value}
        )
        return redirect('grades')
        
    context = {
        'grades': Grade.objects.all(),
        'students': Student.objects.all(),
        'subjects': Subject.objects.all()
    }
    return render(request, 'grades.html', context)
