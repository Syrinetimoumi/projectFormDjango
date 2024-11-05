from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm

def send_email_view(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        
        # Envoyer l'e-mail
        send_mail(
            subject,
            message,
            email,  # L'adresse e-mail de l'expéditeur
            ['sayrouna2019@gmail.com'],  # Remplacez par l'adresse e-mail du destinataire
            fail_silently=False,
        )
        
        # Optionnel : Vous pouvez rediriger ou afficher un message de succès
        return render(request, 'success.html')  # Créez un template de succès

    return render(request, 'email_form.html', {'form': form})  # Créez un template pour le formulaire
