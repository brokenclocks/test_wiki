from django import forms 
from .models import Wiki_page


# creating a form 
class Wiki_Form(forms.ModelForm): 

	# create meta class 
	class Meta: 
		# specify model to be used 
		model = Wiki_Form

		# specify fields to be used 
		fields = [ 
			"title", 
			"description", 
		] 
