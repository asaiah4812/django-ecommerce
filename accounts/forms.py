from django import forms
from django.forms import ModelForm
from . models import Account

class RegisterationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterationForms, self). __init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first Name'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegisterationForms, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.validationError(
                "password does not match"
            )
        