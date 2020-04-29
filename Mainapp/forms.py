from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Mainapp.models import Diary


class Index_form(forms.ModelForm):


    class Meta:
        model = Diary
        fields = ('Eventname', 'desc', 'Location','Date', 'Rating', 'Review')



        # Date = forms.DateField(
        # widget=forms.DateInput(format='%m/%d/%Y'),
        # input_formats=('%m/%d/%Y', )
        # )

class Login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class Registration_form(UserCreationForm): #inheritence
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',

        )

    def save(self, commit=True):
        user= super(Registration_form, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
