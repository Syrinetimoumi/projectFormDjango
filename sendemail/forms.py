from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Objet')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    email = forms.EmailField(label='Votre e-mail')
