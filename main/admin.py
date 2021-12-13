from .models import Customer
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Customer)
class UserAdmin(BaseUserAdmin):

    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_staff')

    fieldsets = (
        (None, {'fields': ('password', )}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )