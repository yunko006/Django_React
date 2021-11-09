from django.contrib import admin
from .models import NewUser

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea



class UserAdminConfig(UserAdmin):
    """
    Customize our admin panel
    """

    # right panel to seach and filter
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff',)

    # main information displayed next to each user
    ordering = ('-start_date',)
    list_display = ('email', 'id', 'user_name', 'first_name', 'is_active', 'is_staff')

    # fieldsets manage the display when we click on a specific user
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personnal', {'fields': ('about',)}),
        )

    # add user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
            }
        ),
    )
admin.site.register(NewUser, UserAdminConfig)
