from django.contrib import admin
from .models import Example


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass
