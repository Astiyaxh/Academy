from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
from user.forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'اطلاعات کاربری',
            {
                'fields':(
                    'national_code','mobile_number1','mobile_number2','birthdate','address','profile_picture',
                )
            }
        )
      
    )


admin.site.register(User, CustomUserAdmin)
