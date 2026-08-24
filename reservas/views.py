from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ReservaForm
from .models import Experiencia, Reserva


def inicio(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inicio')

    else:
        form = ReservaForm()

    experiencias = Experiencia.objects.order_by('orden')

    return render(
        request,
        'index.html',
        {
            'form': form,
            'experiencias': experiencias
        }
    )


def detalle_experiencia(request, id):
    experiencia = get_object_or_404(Experiencia, id=id)

    return render(
        request,
        'detalle_experiencia.html',
        {'experiencia': experiencia}
    )


def reservar_experiencia(request, id):
    experiencia = get_object_or_404(Experiencia, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.experiencia = experiencia
            reserva.lugar = request.POST.get('lugar')
            reserva.save()

            return render(
                request,
                'reserva_exitosa.html'
            )

    else:
        form = ReservaForm()

    return render(
        request,
        'reservar.html',
        {
            'form': form,
            'experiencia': experiencia
        }
    )


def lista_reservas(request):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    reservas = Reserva.objects.all().order_by('-fecha_creacion')

    return render(
        request,
        'lista_reservas.html',
        {
            'reservas': reservas
        }
    )

def editar_reserva(request, id):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    reserva = get_object_or_404(Reserva, id=id)

    if request.method == "POST":

        reserva.nombre = request.POST.get("nombre")
        reserva.correo = request.POST.get("correo")
        reserva.fecha = request.POST.get("fecha")
        reserva.personas = request.POST.get("personas")
        reserva.mensaje = request.POST.get("mensaje")
        reserva.estado = request.POST.get("estado")
        reserva.lugar = request.POST.get("lugar")

        reserva.save()

        return redirect("lista_reservas")

    return render(
        request,
        "editar_reserva.html",
        {
            "reserva": reserva
        }
    )


def eliminar_reserva(request, id):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    reserva = get_object_or_404(Reserva, id=id)

    if request.method == "POST":

        reserva.delete()

        return redirect("lista_reservas")

    return render(
        request,
        "eliminar_reserva.html",
        {
            "reserva": reserva
        }
    )

def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        'attachment; filename="reservas.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setTitle("Reservas NicaExperience")
    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(180, 820, "NicaExperience")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(180, 800, "Informe de Reservas")

    pdf.drawString(
        50,
        780,
        f"Fecha de generación: {datetime.now().strftime('%d/%m/%Y')}"
    )

    reservas = Reserva.objects.all()

    y = 740

    for reserva in reservas:

        pdf.drawString(
            50,
            y,
            f"Código de Reserva: NICA-{reserva.id:04d}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Estado: {reserva.estado}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Cliente: {reserva.nombre}"
        )

        pdf.drawString(
            250,
            y,
            f"Experiencia: {reserva.experiencia}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Lugar: {reserva.lugar}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Correo: {reserva.correo}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Fecha: {reserva.fecha}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Personas: {reserva.personas}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Mensaje: {reserva.mensaje}"
        )


        y -= 50

        if y < 100:
             pdf.showPage()
             pdf.setFont("Helvetica", 12)
             y = 740

    pdf.save()

    return response

from django.contrib import messages

def login_reservas(request):

    if request.method == "POST":

        usuario = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=usuario,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("lista_reservas")
        return render(
            request,
            "login.html",
            {"error": True}
        )

    return render(request, "login.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("login_reservas")

def lista_usuarios(request):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    usuarios = User.objects.all().order_by('username')

    return render(
        request,
        'lista_usuarios.html',
        {
            'usuarios': usuarios
        }
    )

def crear_usuario(request):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("lista_usuarios")

    return render(request,"crear_usuario.html")
    
def editar_usuario(request, id):
    if not request.user.is_authenticated:
        return redirect("login_reservas")

    usuario = User.objects.get(id=id)

    if request.method == "POST":
        usuario.username = request.POST.get("username")
        usuario.first_name = request.POST.get("first_name")
        usuario.last_name = request.POST.get("last_name")
        usuario.email = request.POST.get("email")
        usuario.save()

        return redirect("lista_usuarios")

    return render(
        request,
        "editar_usuario.html",
        {
            "usuario": usuario
        }
    )

def eliminar_usuario(request, id):

    if not request.user.is_authenticated:
        return redirect("login_reservas")

    usuario = User.objects.get(id=id)

    if request.method == "POST":
        usuario.delete()
        return redirect("lista_usuarios")

    return render(
        request,
        "eliminar_usuario.html",
        {
            "usuario": usuario
        }
    )

def granada(request):

     return render(
        request,
        'granada.html'
    )

def masaya(request):

    return render(
      request,
     'masaya.html'
    )

def volcan_masaya(request):
    return render(
        request,
        'volcan_masaya.html'
    )


def rivas(request): 
    
    return render(
       request,
       'rivas.html'
    )

def leon_historico(request):

    return render(
      request, 
      'leon_historico.html'
    )

def managua(request):

    return render(
      request, 
      'managua.html'
    )

def matagalpa(request):

    return render(
      request, 
      'matagalpa.html'
    )

def jinotega(request):

    return render(
      request, 
      'jinotega.html'
    )

def rio_san_juan(request):

    return render(
      request, 
      'rio_san_juan.html'
    )

def chinandega(request):

    return render(
      request, 
      'chinandega.html'
    )

def costa_caribe(request):

    return render(
      request, 
      'costa_caribe.html'
    )



