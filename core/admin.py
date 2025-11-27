from django.contrib import admin
from .models import (
    Teacher,
    Student,
    Staff,
    ClassType,
    Clazz,
    Enrollment,
    Schedule,
    Attendance,
    Feedback
)

# Đăng ký từng model để chúng xuất hiện trên trang admin
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(ClassType)
admin.site.register(Clazz)
admin.site.register(Enrollment)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Feedback)