from django.contrib import admin
from .models import BaseUser

@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ["email", "is_active", "is_admin"]
