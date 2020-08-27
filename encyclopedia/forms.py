from django import forms 
from .models import Wiki_page


# creating a form 
class Wiki_Form(forms.Form):
	title = forms.CharField(max_length=100)
	body = forms.CharField(widget=forms.Textarea)
	 
  