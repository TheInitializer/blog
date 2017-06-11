from django import forms

class CommentForm(forms.Form):
	name = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
