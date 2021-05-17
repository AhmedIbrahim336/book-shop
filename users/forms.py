# get the custome user 
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreatetionForm(UserCreationForm):
    class Meta: 
        model = get_user_model()
        fields = ('email','username')
class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",'username')