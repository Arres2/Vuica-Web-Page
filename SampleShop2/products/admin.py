from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["Codigo", "Nombre","Tallas", "Tipo", "Descripcion", "Imagen", 
    "Hoja_Tecnica"]

class ContactosAdmin(admin.ModelAdmin):
    list_display = ["Nombre","Apellido", "Correo", "Mensaje", "Fecha"]


admin.site.register(Product, ProductAdmin)

