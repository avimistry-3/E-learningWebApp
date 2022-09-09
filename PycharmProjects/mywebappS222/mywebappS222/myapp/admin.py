from django.contrib import admin
import decimal
from django import forms
# Register your models here.
from .models import Topic, Course, Student, Order
# Register your models here.
class CourseInline(admin.TabularInline):
    model = Course

class TopicAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    list_display=('name', 'category')
    def length(self, obj):
        return len(obj.name)
    

class OrderInline(admin.TabularInline):
    model = Order

@admin.action(description='Reduce Price by 10 percent')
def reducePrice(modeladmin, request, queryset):
    
    for course in queryset:
        course.price = course.price * decimal.Decimal('0.9')
        course.save()
        
    

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'for_everyone', 'description')
    actions = [reducePrice, ]


class StudentAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_display = ('first_name','last_name' )
    filter_horizontal = ['interested_in', ]
    def first_name(self,obj):
        return obj.student_name.split()[0]
    
    def last_name(self,obj):
        if(len(obj.student_name.split())>1):
            return obj.student_name.split()[1]
        else:
            return " "

admin.site.register(Topic, TopicAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Order)

