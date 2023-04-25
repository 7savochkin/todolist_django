from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone')
    list_display_links = ('id', 'email', 'phone')
    permissions_fieldsets = {
        'fields': (('is_active', 'is_staff', 'is_superuser'), 'groups',
                   'user_permissions'),
        'classes': ('collapse',),
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'),
         {'fields': ('phone', 'is_valid_phone')}),
        (_('Info'),
         {'fields': ('last_login', 'date_joined', 'is_active')}),
    )
    ordering = ('email',)
