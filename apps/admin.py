from django.contrib import admin
from . import models


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(models.TTJ)
class TTJAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'university')
    list_display_links = ('id', 'title', 'university')


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'student', 'on_ttj')
    list_editable = ('on_ttj',)
    list_display_links = ('id', 'date', 'student')


@admin.register(models.Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'floor', 'room')
    list_display_links = ('id', 'floor', 'room')


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'group', 'floor', 'ttj', 'university', 'phone')
    list_display_links = ('id', 'full_name', 'group', 'floor', 'ttj', 'university', 'phone')


@admin.register(models.Group)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
