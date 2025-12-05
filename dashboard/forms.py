from django import forms
from core.models import Clazz, Teacher, Student, Staff, Enrollment, ClassType, Schedule, Attendance

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ClassForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clazz
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TeacherForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('user',) # Exclude user field as it might be auto-assigned or managed separately
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class StaffForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class EnrollmentForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ClassTypeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ClassType
        fields = '__all__'

class ScheduleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class AttendanceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }