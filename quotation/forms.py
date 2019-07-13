from django import forms
from .models import Quote

class quote_form(forms.ModelForm):

	class Meta():
		model = Quote
		fields = ['material', 'finishes', 'quantity', 'name', 'contact_no', 'emailid']