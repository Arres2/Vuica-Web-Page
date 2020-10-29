from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        last_name  = request.POST["last_name"]
        empresa = request.POST["empresa"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]


        send_mail(subject= subject, message= "De: "+ name + " " + last_name + "\n" + "Correo: " + email + "\n" + "Empresa: " + empresa + "\n\n" + "Mensaje: " + message, from_email = email, recipient_list = [email, 'andrescvuica@gmail.com'])
        
        return HttpResponse("Gracias, le estaremos contestando pronto!") 

    else:
        return render(request, "index.html")

    

    

