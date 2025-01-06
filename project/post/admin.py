from django.contrib import admin

# Register your models here.
from .models import Author
from .models import todo

admin.site.register(Author)
class ascendingDeadline(admin.ModelAdmin):
  ordering = ['deadline_date']


  
admin.site.register(todo,ascendingDeadline)