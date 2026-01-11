from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    ordering = ['-date_joined']

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'address')}),
    )
