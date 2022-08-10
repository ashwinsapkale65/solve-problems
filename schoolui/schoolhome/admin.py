from tabnanny import check
from django.contrib import admin

# Register your models here.

from schoolhome.models import User,studentregistrations,teacherregistrations,checkstudent
admin.site.register(User)

admin.site.register(teacherregistrations)
admin.site.register(studentregistrations)
admin.site.register(checkstudent)

