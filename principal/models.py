# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apicultura(models.Model):
    nombre = models.CharField(max_length=45)
    feinicio = models.DateField()
    fefin = models.DateField()
    especies = models.CharField(max_length=225)
    cantcolmenas = models.IntegerField()
    polifloracion = models.CharField(max_length=225)
    medicion_sensor = models.ForeignKey('Msensor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apicultura'


class Ciudad(models.Model):
    nombre = models.CharField(max_length=45)
    cpostal = models.IntegerField()
    ciudad = models.CharField(max_length=45)
    departamentos = models.ForeignKey('Departamentos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    pnombre = models.CharField(max_length=45)
    snombre = models.CharField(max_length=45)
    papellido = models.CharField(max_length=45)
    sapellido = models.CharField(max_length=45)
    genero = models.CharField(max_length=9)
    tp_cliente = models.ForeignKey('Tcliente', models.DO_NOTHING)
    contrato = models.ForeignKey('Contrato', models.DO_NOTHING)
    direccion = models.ForeignKey('Direccion', models.DO_NOTHING)
    tipo_identificacion = models.ForeignKey('Tdentificacion', models.DO_NOTHING, db_column='Tipo_identificacion_id')  # Field name made lowercase.
    telefono = models.IntegerField()
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contrato(models.Model):
    feinicio = models.DateField()
    fefinal = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=45)
    cultivo = models.ForeignKey('Cultivo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contrato'


class Cultivo(models.Model):
    descripcion = models.CharField(max_length=200)
    piscicultura = models.ForeignKey('Piscicultura', models.DO_NOTHING)
    apicultura = models.ForeignKey(Apicultura, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cultivo'


class Departamentos(models.Model):
    nombre = models.CharField(max_length=45)
    pais = models.ForeignKey('Pais', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Direccion(models.Model):
    calle = models.CharField(max_length=45, blank=True, null=True)
    carrera = models.CharField(max_length=45, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direccion'


class Infotrata(models.Model):
    nombre = models.TextField()
    feinicio = models.DateField()
    fefin = models.DateField()

    class Meta:
        managed = False
        db_table = 'infotrata'


class Msensor(models.Model):
    fechahora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'msensor'
        
    # def __str__(self) -> str:
    #     return self


class Pais(models.Model):
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'pais'


class Piscicultura(models.Model):
    nombre = models.CharField(max_length=45)
    feinicio = models.DateField()
    fefinal = models.DateField()
    especies = models.CharField(max_length=150)
    cantpeces = models.IntegerField()
    alimentacion = models.CharField(max_length=150)
    frecualimentacion = models.CharField(max_length=150)
    tiemcultivo = models.IntegerField()
    medicion_sensor = models.ForeignKey(Msensor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'piscicultura'


class Sensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)
    tipo_sensor = models.ForeignKey('Tsensor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sensor'


class Tcliente(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tcliente'


class Tdentificacion(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tdentificacion'


class Tiptrata(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'tiptrata'


class Tratamiento(models.Model):
    fecha_aplicacion = models.DateField()
    dosis = models.FloatField()
    resultado = models.CharField(max_length=250)
    apicultura = models.ForeignKey(Apicultura, models.DO_NOTHING)
    informacion_tratamiento = models.ForeignKey(Infotrata, models.DO_NOTHING)
    tipo_tratamiento = models.ForeignKey(Tiptrata, models.DO_NOTHING)
    piscicultura = models.ForeignKey(Piscicultura, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tratamiento'
        unique_together = (('id', 'apicultura', 'informacion_tratamiento', 'piscicultura'),)


class Tsensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tsensor'
