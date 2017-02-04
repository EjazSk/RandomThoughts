from django import forms
from .models import RT

class RT_Form(forms.ModelForm):
	class Meta:
		model=RT
		fields=['thought','public']