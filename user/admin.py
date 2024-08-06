from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "first_name",
        "last_name",
        "address",
        "role",
    ]
