from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Include custom fields in the admin interface
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the custom user model with the admin
admin.site.register(CustomUser, CustomUserAdmin)
