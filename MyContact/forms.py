from django import forms

class contactform2(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    Email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)


from django.forms import ModelForm
from .models import Contact

class contactForm3(ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'message']
