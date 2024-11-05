from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact





# Create your views here.
def controleform1(request):
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']
       
        # Create the Contact object
        contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        #contact=Contact(firstname=f,lastname=l,Email=e,msg=m)

        contact.save()  # This line is not necessary since create() already saves it

        return HttpResponse('<h2> Data has been submitted </h2>')

    return render(request, "myform1.html")  # Return the form if not a POST request


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import contactform2
from .models import Contact

def controleform2(request):
    if request.method == 'POST':  # Si la requête est POST
        form = contactform2(request.POST)  # Nous reprenons les données
        if form.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['Email']
            msg = form.cleaned_data['msg']

            # Enregistrement dans la base de données
            contact = Contact.objects.create(firstname=firstname, lastname=lastname, Email=email, msg=msg)

            return HttpResponse('<h2> Data has been submitted </h2>')
    else:
        form = contactform2()  # Afficher le formulaire vide

    return render(request, "myform2.html", {'mycontactform2': form})

from .forms import contactForm3

def controleform3(request):
    if request.method == "POST":
        form = contactForm3(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myform3.html', {'message': 'Formulaire enregistré avec succès', 'form': form})
    else:
        form = contactForm3()
    return render(request, 'myform3.html', {'form': form})

