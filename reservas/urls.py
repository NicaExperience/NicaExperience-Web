from django.urls import path
from . import api_views

from .views import (
    inicio,
    detalle_experiencia,
    reservar_experiencia,
    lista_reservas,
    editar_reserva,
    eliminar_reserva,
    generar_pdf,
    login_reservas,
    cerrar_sesion,
    lista_usuarios,
    crear_usuario,
    editar_usuario,
    eliminar_usuario,
    granada,
    masaya,
    volcan_masaya,
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
    'reservas/editar/<int:id>/',
    editar_reserva,
    name='editar_reserva'
     ),

path(
    'reservas/eliminar/<int:id>/',
    eliminar_reserva,
    name='eliminar_reserva'
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
    'usuarios/crear/',
    crear_usuario,
    name='crear_usuario'
    ),

path(
    'usuarios/editar/<int:id>/',
    editar_usuario,
    name='editar_usuario'
    ),

path(
    'usuarios/eliminar/<int:id>/',
    eliminar_usuario,
    name='eliminar_usuario'
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

path(
    'volcan_masaya/',
    volcan_masaya,
    name='volcan_masaya'
     ),

path(
    'api/experiencias/',
    api_views.api_experiencias,
    name='api_experiencias'
),

path(
    'api/experiencias/<int:id>/',
    api_views.api_experiencia_detalle,
    name='api_experiencia_detalle'
),

path(
    'api/reservas/',
    api_views.api_reservas,
    name='api_reservas'
),

]





