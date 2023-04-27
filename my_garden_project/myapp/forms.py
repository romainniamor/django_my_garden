
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField
from .models import *


def validate_email_unique(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError('Cette adresse e-mail est déjà utilisée.')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Pseudo...'}))
    email = forms.EmailField(label="", validators=[validate_email_unique], widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe...'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirmation...'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DepartementModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nom

class ProfileForm(forms.ModelForm):
    departement = DepartementModelChoiceField(label='',
                                              required=True,
                                              queryset=Departement.objects.all(),
                                              empty_label='Votre département...')

    class Meta:
        model = Profile
        fields = ['departement']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'placeholder': 'Ancien mot de passe...'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Nouveau mot de passe...'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirmez le nouveau mot de passe...'})


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Ecrivez votre adresse e-mail...'})





