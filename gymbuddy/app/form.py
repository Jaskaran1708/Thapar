from django import forms
from .models import  Customer, Complaints, User
from django.contrib.auth.forms import UserCreationForm


class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = [ 'first_name', 'last_name','email',  'phone_number' ]
    widgets = {'email':forms.TextInput(attrs={'class':'form-control'}), 'first_name':forms.TextInput(attrs={'class':'form-control'}), 
    'last_name':forms.TextInput(attrs={'class':'form-control'}),
    'phone_number':forms.NumberInput(attrs={'class':'form-control'})}

class ComplaintForm(forms.ModelForm):
  class Meta:
    model = Complaints
    fields = ['title','description', 'image']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
