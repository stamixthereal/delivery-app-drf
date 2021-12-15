from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Customer, Product, Restaurant


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customer
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'
        )
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
            }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Customer, CustomUserAdmin)

admin.site.register(Product)

admin.site.register(Restaurant)