from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Experiencia, Reserva
from .serializers import ExperienciaSerializer, ReservaSerializer


@api_view(['GET'])
def api_experiencias(request):
    experiencias = Experiencia.objects.order_by('orden')
    serializer = ExperienciaSerializer(
        experiencias,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def api_experiencia_detalle(request, id):
    try:
        experiencia = Experiencia.objects.get(id=id)

    except Experiencia.DoesNotExist:
        return Response(
            {'error': 'Experiencia no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ExperienciaSerializer(experiencia)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_reservas(request):

    if request.method == 'GET':

        reservas = Reserva.objects.all().order_by(
            '-fecha_creacion'
        )

        serializer = ReservaSerializer(
            reservas,
            many=True
        )

        return Response(serializer.data)

    if request.method == 'POST':

        serializer = ReservaSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )