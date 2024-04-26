from django import forms
from .models import student


# class studentform(forms.Form):
    
#     profile = forms.ImageField(max_length=255)
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
#     email = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
    
class studentform(forms.ModelForm):
    class  Meta:
        model = student
        fields = ['profile', 'first_name', 'last_name', 'email', 'password']