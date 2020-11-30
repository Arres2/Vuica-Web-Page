from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.core.mail import send_mail

def productos(request):
    productos = Product.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        last_name  = request.POST["last_name"]
        empresa = request.POST["empresa"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]


        send_mail(subject= subject, message= "De: "+ name + " " + last_name + "\n" + "Correo: " + email + "\n" + "Empresa: " + empresa + "\n\n" + "Mensaje: " + message, from_email = email, recipient_list = [email, 'ventasvuica@gmail.com','paginawebvuica@gmail.com'])
        
        return HttpResponse("Gracias, le estaremos contestando pronto!") 

    else:
        return render(request,"productos.html", {"productos": productos})

    


def detalles(request, Codigo):
    obj = get_object_or_404(Product, Codigo=Codigo)

    context = {
        "Codigo": obj.Codigo,
        "Nombre":obj.Nombre,
        "Tipo":obj.Tipo,
        "Talla":obj.Tallas,
        "Unidades":obj.Unidades,
        "Hoja_Tecnica": obj.Hoja_Tecnica,
        "Descripcion": obj.Descripcion,
        "Imagen":obj.Imagen
    }

    if request.method == "POST":
        name = request.POST["name"]
        last_name  = request.POST["last_name"]
        empresa = request.POST["empresa"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]


        send_mail(subject= subject, message= "De: "+ name + " " + last_name + "\n" + "Correo: " + email + "\n" + "Empresa: " + empresa + "\n\n" + "Mensaje: " + message, from_email = email, recipient_list = [email, 'ventasvuica@gmail.com','paginawebvuica@gmail.com'])
        
        return HttpResponse("Gracias, le estaremos contestando pronto!") 

    else:
        return render(request,"productos-detalles.html", context)

  
    



