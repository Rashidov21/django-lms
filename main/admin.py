from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'duration')
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'course', 'lesson_start_time', 'lesson_end_time', 'lesson_started_date', 'lesson_days')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug', 'phone', 'address', 'group', 'status')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug', 'phone', 'address', 'contract_type', 'contract_percent_value', 'contract_student_value')