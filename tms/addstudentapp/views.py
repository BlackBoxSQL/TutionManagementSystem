from django.shortcuts import render, redirect
from . forms import StudentregistrationForm, PaymentForm, AttendenceForm, ResultForm, SheetForm
from . models import Studentregistration, Result, Sheet
# Create your views here.


def homepage(request):
    return render(request, 'addstudentapp/homepage.html')


def addstudent(request):
    if request.method == "POST":
        addstudent = StudentregistrationForm(request.POST)
        if addstudent.is_valid():
            post = addstudent.save(commit=False)
            post.save()
            return redirect('addstudent')
    else:
        addstudent = StudentregistrationForm()

    return render(request, 'addstudentapp/addstudent.html', {'addstudent': addstudent})


def allstudents(request):
    context = {
        'students': Studentregistration.objects.all(),
    }

    return render(request, 'addstudentapp/allstudents.html', context)


def payment(request):
    if request.method == "POST":
        addpayment = PaymentForm(request.POST)
        if addpayment.is_valid():
            post = addpayment.save(commit=False)
            post.save()
            return redirect('payment')
    else:
        addpayment = PaymentForm()

    return render(request, 'addstudentapp/payment.html', {'addpayment': addpayment})


def takeattendence(request):
    if request.method == "POST":
        attendence = AttendenceForm(request.POST)
        if attendence.is_valid():
            post = attendence.save(commit=False)
            post.save()
            return redirect('takeattendence')
    else:
        attendence = AttendenceForm()

    return render(request, 'addstudentapp/attendence.html', {'attendence': attendence})


def result(request):
    pass


def sheet(request):
    pass
