from django.http import HttpResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
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
    if not request.session.get("admin"):
       return redirect("login_reservas")
    reservas = Reserva.objects.all().order_by('-fecha_creacion')

    return render(
        request,
        'lista_reservas.html',
        {
            'reservas': reservas
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

        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        if usuario == "admin" and password == "1234":

            request.session["admin"] = True

            return redirect("lista_reservas")

        return render(
            request,
            "login.html",
            {"error": True}
        )

    return render(request, "login.html")

def granada(request):

     return render(
        request,
        'granada.html'
    )

def volcan_masaya(request):

    return render(
      request,
     'volcan_masaya.html'
    )










