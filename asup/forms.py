from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=5)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        
        widgets = {
            'username': forms.TextInput({'class':'form-control','minlength':'5'}),
            'email': forms.EmailInput({'class':'form-control'})
        }


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['password1'].label = "Password"
        self.fields['username'].help_text = None

class LoginForm(UserCreationForm):
    # untuk ganti nama input
    custom_names = {'password1': 'password'}
    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super(LoginForm, self).add_prefix(field_name)
        
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=5)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','name':'password'}), min_length=5)
    
    class Meta:
        model = User
        fields = ['username', 'password1']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['password1'].label = "Password"
        self.fields['username'].help_text = None