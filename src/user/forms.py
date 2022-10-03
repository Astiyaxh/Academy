from django.contrib.auth.forms import UserCreationForm
from user.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__" 


class UpdateProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__" 
        exclude = ("id", "last_login", "is_superuser", "is_staff", "is_active", "date_joined")