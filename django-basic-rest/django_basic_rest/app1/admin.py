from django.contrib import admin
from .models import Note, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Note)