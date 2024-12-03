from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm



# create
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

# read
def students_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query) | Student.objects.filter(course__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

# update
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form})

# delete
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('students_list')
    return render(request, 'students/confirm_delete.html', {'student': student})

