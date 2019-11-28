from django import forms

from .models import Studentregistration, Payment


class StudentregistrationForm(forms.ModelForm):

    class Meta:
        model = Studentregistration
        fields = ('student_name', 'student_phone',
                  'guardians_phone', 'college', 'year', 'address',)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('student_name', 'month', 'paid',)
