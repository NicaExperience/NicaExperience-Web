from django.urls import path

from .views import (
    inicio,
    detalle_experiencia,
    reservar_experiencia,
    lista_reservas,
    generar_pdf,
    login_reservas,
    cerrar_sesion,
    lista_usuarios,
    crear_usuario,
    granada,
    masaya,
    rivas,
    leon_historico,
    managua,
    matagalpa,
    jinotega,
    rio_san_juan,
    chinandega,
    costa_caribe,
    
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
    'logout/',
    cerrar_sesion,
    name='cerrar_sesion'
),

path(
    'usuarios/',
    lista_usuarios,
    name='lista_usuarios'
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

path(
    'masaya/',
    masaya,
    name='masaya'
    ),

path(
    'rivas/',
    rivas,  
    name='rivas'
    ),

path(
    'leon_historico/',
    leon_historico,
    name='leon_historico'
    ),

path(
    'managua/',
    managua,
    name='managua'
    ),

path(
    'matagalpa/',
    matagalpa,
    name='matagalpa'
    ),

path(
    'jinotega/',
    jinotega,
    name='jinotega'
    ),

path(
    'rio_san_juan/',
    rio_san_juan,
    name='rio_san_juan'
    ),

path(
    'chinandega/',
    chinandega,
    name='chinandega'
    ),

path(
    'costa_caribe/',
    costa_caribe,
    name='costa_caribe'
    ),

]





