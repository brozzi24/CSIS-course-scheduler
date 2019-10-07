from django.contrib import admin

from .models import Classes

# Register your models here.
class ClassesAdmin(admin.ModelAdmin):
    list_display = ('id','name','course_number','subject','special','grad_type')
    list_display_links = ('id','name','course_number')
    list_filter = ('subject','grad_type')
   
    list_per_page = 25


admin.site.register(Classes, ClassesAdmin)