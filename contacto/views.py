from django.shortcuts import render, redirect

from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formularioContacto = ContactoForm()

    if request.method == "POST":
        formularioContacto = ContactoForm(data=request.POST)
        if formularioContacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde tu pagina web",
                                 "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}"
                                 .format(nombre, email, contenido),
                                 "Tu web",
                                 ['ledfullstarter@gmail.com'],
                                 reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, 'contacto/contacto.html', {'formularioContacto': formularioContacto})
