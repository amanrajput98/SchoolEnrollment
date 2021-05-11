from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'fathers_name', 'dob', 'address', 'city', 'state', 'pin',
        'phone', 'email', 'class_enrolled', 'marks', 'enrollment_date'
        ]

