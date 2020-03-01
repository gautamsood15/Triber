from django import forms
from django.core.exceptions import ValidationError
from .models import Tweet

class TweetModelForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = [
			"user",
			"content"
		]
		#exclude = ['']

	#def clean_content(self, *args, **kwargs):
	#	content = self.cleaned_data("content")
	#	if content == "abc":
	#		raise forms.ValidationError("Cannot be ABC")
	#	return content