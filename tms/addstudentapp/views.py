from django.shortcuts import render, redirect
from . forms import StudentregistrationForm, PaymentForm
from . models import Studentregistration
# Create your views here.


def homepage(request):
    return render(request, 'addstudentapp/homepage.html')


def addstudent(request):
    if request.method == "POST":
        addstudent = StudentregistrationForm(request.POST)
        if addstudent.is_valid():
            post = addstudent.save(commit=False)
            post.save()
            return redirect('homepage')
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
            return redirect('homepage')
    else:
        addpayment = PaymentForm()

    return render(request, 'addstudentapp/payment.html', {'addpayment': addpayment})
