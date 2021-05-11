from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.


def show_students(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Stude
            print('VAlid form')
            student_name = form.cleaned_data.get("student_name")
            fathers_name = form.cleaned_data.get("fathers_name")
            dob = form.cleaned_data.get("dob")
            address = form.cleaned_data.get("address")
            city = form.cleaned_data.get("city")
            state = form.cleaned_data.get("state")
            pin = form.cleaned_data.get("pin")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            class_enrolled = form.cleaned_data.get("class_enrolled")
            marks = form.cleaned_data.get("marks")
            enrollment_date = form.cleaned_data.get("enrollment_date")

            new_student = Student(student_name=student_name, fathers_name=fathers_name, dob=dob, address=address,
                city=city, state=state, pin=pin, phone=phone, email=email, class_enrolled=class_enrolled,
                marks=marks, enrollment_date=enrollment_date)
            new_student.save()
            student_form = StudentForm()
            context = {'student_form': student_form}
            return render(request, 'index.html', context=context)
        else:
            print('Invalid form')
            return render(request, 'index.html', context={'student_form': form})
    else:
        form = StudentForm()
        student_list = []
        for student in Student.objects.all():
            student_list.append({'name': student.student_name, 'email': student.email,
            'phone': student.phone, 'class': student.class_enrolled,
            'marks': student.marks})

        context = {'student_form': form, 'student_list': student_list}
        return render(request, 'index.html', context=context)
