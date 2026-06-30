from django.urls import path

from .views import (
    inicio,
    detalle_experiencia,
    reservar_experiencia,
    lista_reservas,
    generar_pdf,
    login_reservas,
    granada
)

urlpatterns = [
    path('', inicio, name='inicio'),

    path(
        'experiencia/<int:id>/',
        detalle_experiencia,
        name='detalle_experiencia'
    ),

    path(
        'reservar/<int:id>/',
        reservar_experiencia,
        name='reservar_experiencia'
    ),

    path(
        'reservas/',
        lista_reservas,
        name='lista_reservas'
    ),

path(
    'login/',
    login_reservas,
    name='login_reservas'
     ),

path(
     'pdf/',
     generar_pdf,
    name='generar_pdf'
    ),

path(
     'granada/',
     granada,
     name='granada'
    ),

]



