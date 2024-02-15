from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["user_image", "username", "email", "first_name", "last_name", "is_staff"]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ('first_name', 'last_name', 'email', 'image', 'job', 'address')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def user_image(self, obj: User):
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="{obj.image.url}" width="35" height="35" style="object-fit: cover;"></a>'
        )

    user_image.short_description = 'Image'
