from django.db import models

ESTADOS = [
    ('Pendiente', 'Pendiente'),
    ('Confirmada', 'Confirmada'),
    ('Cancelada', 'Cancelada'),
    ('Finalizada', 'Finalizada'),
]

class Reserva(models.Model):
    experiencia = models.ForeignKey(
        'Experiencia',
        on_delete=models.CASCADE,
        null=True,
        blank=True
  )

    lugar = models.CharField(
    max_length=100,
    blank=True,
    null=True

  )

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha = models.DateField()
    personas = models.PositiveIntegerField()
    mensaje = models.TextField(blank=True)
    estado = models.CharField(max_length=20,default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ubicacion = models.CharField(max_length=100, default="")
    duracion = models.CharField(max_length=50, default="")
    
    def __str__(self): 
         return self.titulo 



    

   