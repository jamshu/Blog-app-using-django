from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=32)
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 4}))
    
