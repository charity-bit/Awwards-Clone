from django.contrib import admin
from .models import Category,Project,Tags,Vote

# Register your models here.
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Tags)
admin.site.register(Vote)