from django.contrib import admin

# Register your models here.
from .models import Post
from .models import FormData
class ascendingDeadline(admin.ModelAdmin):
  ordering = ['deadline_date']

admin.site.register(Post)
# admin.site.register(FormData)