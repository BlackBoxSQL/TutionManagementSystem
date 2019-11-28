from django import forms

from .models import Studentregistration


class StudentregistrationForm(forms.ModelForm):

    class Meta:
        model = Studentregistration
        fields = ('student_name', 'student_phone',
                  'guardians_phone', 'college', 'year', 'address',)
