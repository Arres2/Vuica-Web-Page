from django.db import models
from django.urls import reverse


class Product(models.Model):
    Codigo = models.CharField(max_length=20, primary_key=True)

    talla = [
        ("Todas","Todas"),
        ("No Aplica","N/A"),
        ("Única","Unica")
        ]
    
    tipo_producto = [
        ("respiratoria", "Protección Respiratoria"),
        ("guantes", "Guantes"),
        ("calzado", "Calzado"),
        ("auditiva", "Protección Auditiva"),
        ("cabeza", "Protección Ojos, Cara y Cabeza"),
        ("vestuario", "Vestuario"),
        ("señalizacion", "Señalización"),
        ("ergonomia y Protección de Caídas", "Ergonomía y Protección de Caídas"),
        ("absorbentes y Paños", "Absorbentes y Paños"),
        ("auxilios", "Primeros Auxilios"),
        ("adhesivos", "Adhesivos, Cintas y Tapes")
        ]

    Unit = [
        ("Par","PAR"),
        ("Paquete", "PQT"),
        ("Paquete de 8", "PQT8"),
        ("Pieza", "PZA"),
        ("Cajita de 100", "CJTA100"),
        ("Cajita de 50", "CJTA50"),
        ("Conjunto", "CONJ"),
        ("Rollo", "ROLL"),
        ("Tubo","TB")

    ]

    
    Nombre = models.CharField(max_length=100)
    Tallas = models.CharField(max_length=15, choices=talla)
    Unidades = models.CharField(max_length=15, choices=Unit)
    Tipo = models.CharField(max_length=50, choices=tipo_producto)
    Descripcion = models.TextField(max_length=None)
    Imagen = models.ImageField(upload_to="Imagen")
    Hoja_Tecnica = models.FileField(upload_to="Hoja_Tecnica")

    def get_absolute_url(self):
        return reverse("products:productos-detalles", kwargs={"Codigo": self.Codigo})



 