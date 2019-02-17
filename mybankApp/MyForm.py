from django import forms

class myForm(forms.Form):
   user = forms.CharField(max_length = 50)