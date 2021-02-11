from django.shortcuts import render, redirect, get_object_or_404
from .models import Student_store_model
from .forms import student_Edit_form


# Create your views here.

def Homepage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')

        data = Student_store_model(Name=name, Email=email, Department=department)
        data.save()
        return redirect("homepage")

    total_student = Student_store_model.objects.all()
    query_data = {
        "total_Student": total_student
    }
    return render(request, 'index.html', query_data)


def Edit(request, id):
    student_id = get_object_or_404(Student_store_model, id=id)
    edit_student = student_Edit_form(instance=student_id)
    if request.method == "POST":
        form = student_Edit_form(request.POST, instance=student_id)
        if form.is_valid:
            form.save()
            return redirect('/')

    query_data = {
        "form": edit_student,
    }

    return render(request, 'update.html', query_data)


def Delete(request, id):
    student_id = get_object_or_404(Student_store_model, id=id)
    student_id.delete()
    return redirect('/')
