
# inbuilt library to create form fields attributes
from django import forms

# To create form structure and restriction import this
from django.contrib.auth.forms import UserCreationForm

# stor user in this model
from django.contrib.auth.models import User


#For registration of user

class UserCreate(UserCreationForm):
    # Giving restriction to the some form attributes
    #Bank end validation
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Optional.')  # necessary if required=True
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    # structure
    class Meta:
        # Store these data in this model
        model = User

        # Take these values from user and check
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email')
