from django.contrib.auth.forms import UserCreationForm
from user.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__" 


class UpdateProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'national_code', 'mobile_number1', 'mobile_number2', 'birthdate', 'address', 'profile_picture']