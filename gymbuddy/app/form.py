from django import forms
from .models import  Customer

class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = [ 'first_name', 'last_name','email',  'phone_number' ]
    widgets = {'email':forms.TextInput(attrs={'class':'form-control'}), 'first_name':forms.TextInput(attrs={'class':'form-control'}), 
    'last_name':forms.TextInput(attrs={'class':'form-control'}),
    'phone_number':forms.NumberInput(attrs={'class':'form-control'})}