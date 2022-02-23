
from email import message
from django.shortcuts import render, redirect
from .models import Employee, Project
from .forms import EmployeeForm, Projectform
from django.contrib import messages
# Create your views here.


def welcome(request):
    te = Employee.objects.all().count()
    tp = Project.objects.all().count()
    return render(request, "welcome.html", {'te': te, 'tp': tp})


def addproject(request):
    form = Projectform
    return render(request, 'project.html', {'pr': form})


def addprd(request):
    ft = Projectform(request.POST)
    if ft.is_valid():

        ft.save()
        return redirect('/showproject')
    else:
        # for i in ft:
        # if i.errors:
        #     print(i.name)
        return render(request, 'error.html', {'context': ft})


def load_form(request):
    form = EmployeeForm
    return render(request, "index.html", {'form': form})


def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    employee = Employee.objects.all().order_by('id')
    return render(request, "show.html", {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    prm = Project.objects.all().order_by('id')
    return render(request, 'edit.html', {'employee': employee, 'prm': prm})


def update(request, id):
    employee = Employee.objects.get(id=id)

    form = EmployeeForm(request.POST, instance=employee)

    # for field in form:
    # print("Field Error:", field.name,  field.errors)
    form.save()
    return redirect('/show')
    # return redirect('/show')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def showproject(request):
    project = Project.objects.all().order_by('id')

    if request.method == 'GET':
        context = {'project': project}
    else:
        employee = Employee.objects.filter(projectid=request.POST['pid'])
        context = {'Employee': employee, 'project': project}

    return render(request, "showproject.html", context)
