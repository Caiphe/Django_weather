from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["username"].widget.attrs["placeholder"] = "Nom d'utilisateur *"
        self.fields["email"].label = ''
        self.fields["email"].widget.attrs["placeholder"] = "Addresse Email  *"
        self.fields["password1"].widget.attrs["placeholder"] = "Password *"
        self.fields["password2"].label = ''
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password *"


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ''
        self.fields["username"].widget.attrs["placeholder"] = "Nom d'utilisateur *"
        self.fields["password"].label = ''
        self.fields["password"].widget.attrs["placeholder"] = "Mot de Passe *"
