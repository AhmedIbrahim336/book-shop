# get the custome user 
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    # the password in already includes 
    class Meta: 
        model = get_user_model()
        fields = ('email','username')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",'username')