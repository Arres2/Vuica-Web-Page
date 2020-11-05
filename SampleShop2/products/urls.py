from . import views
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
#
#//products/1/detail
#/products/new


app_name= 'products'

urlpatterns = [
    path("", views.productos, name="Lista_de_Productos"),
    path("<str:Codigo>/", views.detalles),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





