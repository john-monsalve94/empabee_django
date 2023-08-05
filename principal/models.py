# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class AsignacionEncargado(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_inicial = models.CharField(max_length=45, blank=True, null=True)
    fecha_final = models.CharField(max_length=45, blank=True, null=True)
    persona = models.ForeignKey('Persona', models.DO_NOTHING)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'asignacion_encargado'


class CabezaFactura(models.Model):
    id = models.IntegerField(primary_key=True)
    cabeza_facturacol = models.CharField(max_length=45, blank=True, null=True)
    empresa = models.ForeignKey('Empresa', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cabeza_factura'


class Ciudad(models.Model):
    nombre = models.CharField(max_length=45, db_comment='nombre de la ciudad')
    codigo = models.IntegerField(db_comment='codigo de la ciudad')
    c_postal = models.IntegerField(
        blank=True, null=True, db_comment='codigo postal de la ciudad')
    departamentos = models.ForeignKey('Departamentos', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'ciudad'
        db_table_comment = 'Tabla utilizada para guardar nombres ,codigos postales y codigos de ciudad'


class Colmena(models.Model):
    nombre = models.CharField(max_length=45, db_comment='Nombre: Este campo almacena el nombre o identificacin de un registro especfico relacionado con la apicultura. Puede ser el nombre de un apicultor, una granja de abejas o cualquier otro nombre que ayude a identificar la entrada en la base de datos.')
    feinicio = models.DateField(db_comment='Fecha inicio: Este campo registra la fecha en la que comenz un evento o perodo relevante para la apicultura. Puede representar la fecha de inicio de una temporada de cosecha, el inicio de un proyecto especfico o cualquier otro evento relacionado con la apicultura.')
    fefin = models.DateField(db_comment='Fecha final: Este campo almacena la fecha en la que termina un evento o perodo relacionado con la apicultura. Puede ser la fecha de finalizacin de una temporada de cosecha, el final de un proyecto especfico o cualquier otro evento relevante.')
    especies = models.CharField(max_length=225, db_comment='Especies: Este campo registra las especies de abejas presentes en una ubicacin especfica. Puede incluir diferentes tipos de abejas, como Apis mellifera (abeja de la miel).\nApis mellifera: tambin conocida como abeja de la miel europea, es la especie de abeja melfera ms comnmente utilizada en la apicultura a nivel mundial.\nApis cerana: una especie de abeja melfera nativa de Asia, tambin utilizada en la apicultura en algunas regiones.\nApis dorsata: conocida como abeja gigante, es una especie de abeja melfera que se encuentra en el sudeste asitico y algunas partes de la India.\nApis florea: una especie de abeja melfera ms pequea que se encuentra en regiones de Asia y frica.\nApis andreniformis: otra especie de abeja melfera nativa de Asia.')
    polifloracion = models.CharField(max_length=225, db_comment='Poli floracin: Este campo indica si hay poli floracin en la ubicacin o evento relacionado con la apicultura. La poli floracin se refiere a la presencia de mltiples especies de flores o plantas que proporcionan nctar y polen a las abejas. Puede ser un factor importante para el xito y la productividad de las colmenas.')
    cultivo = models.ForeignKey('Cultivo', models.DO_NOTHING)
    especie_abeja = models.ForeignKey('EspecieAbeja', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'colmena'


class Contrato(models.Model):
    feinicio = models.DateField()
    fefinal = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=45)
    cultivo = models.ForeignKey('Cultivo', models.DO_NOTHING)
    t_contrato = models.ForeignKey('TContrato', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'contrato'


class CuerpoFactura(models.Model):
    id = models.IntegerField(primary_key=True)
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    cabeza_factura = models.ForeignKey(CabezaFactura, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cuerpo_factura'


class Cultivo(models.Model):
    nombre_cultivo = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'cultivo'


class Departamentos(models.Model):
    nombre = models.CharField(
        max_length=45, db_comment='nombre del departamento')
    codigo = models.IntegerField(db_comment='codigo del departamento')
    pais = models.ForeignKey('Pais', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'departamentos'
        db_table_comment = 'Tabla usada para guardar nombres de departamentos'


class Direccion(models.Model):
    calle = models.CharField(max_length=45)
    carrera = models.CharField(max_length=45, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)
    ciudad_departamentos_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'direccion'
        db_table_comment = 'esta tabla guarda las direcciones donde puedes encontrar una empresa'


class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    nit = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.ForeignKey(Direccion, models.DO_NOTHING)
    t_empresa = models.ForeignKey('TEmpresa', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'empresa'
    
    def __str__(self) -> str:
        return self.nombre
    

class EspecieAbeja(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = True
        db_table = 'especie_abeja'


class EspeciePez(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'especie_pez'


class Estanque(models.Model):
    nombre = models.CharField(max_length=45)
    feinicio = models.DateField()
    fefinal = models.DateField()
    especies = models.CharField(max_length=150)
    cantpeces = models.IntegerField()
    alimentacion = models.CharField(max_length=150)
    frecualimentacion = models.CharField(max_length=150)
    tiemcultivo = models.IntegerField()
    cultivo = models.ForeignKey(Cultivo, models.DO_NOTHING)
    especie_pez = models.ForeignKey(EspeciePez, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'estanque'


class InfotrataColmena(models.Model):
    nombre = models.TextField()
    f_inicio = models.DateField()
    f_fin = models.DateField(blank=True, null=True)
    infotrata_colmenacol = models.IntegerField(blank=True, null=True)
    colmena = models.ForeignKey(Colmena, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'infotrata_colmena'


class InfotrataEstanque(models.Model):
    nombre = models.TextField()
    f_inicio = models.DateField()
    f_fin = models.DateField()
    tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING)
    estanque_id = models.IntegerField()
    estanque_id1 = models.ForeignKey(
        Estanque, models.DO_NOTHING, db_column='estanque_id1')

    class Meta:
        managed = True
        db_table = 'infotrata_estanque'
        unique_together = (('id', 'estanque_id'),)


class MSensorColmena(models.Model):
    fechahora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)
    colmena = models.ForeignKey(Colmena, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'm_sensor_colmena'

    def __str__(self) -> str:
        return self.fechahora


class MSensorEstanque(models.Model):
    fechahora = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    sensor = models.ForeignKey('Sensor', models.DO_NOTHING)
    estanque = models.ForeignKey(Estanque, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'm_sensor_estanque'


class Pais(models.Model):
    nombre = models.CharField(max_length=45, db_comment='nombre del pais')
    codigo = models.IntegerField(db_comment='Codigo del pais')

    class Meta:
        managed = True
        db_table = 'pais'
        db_table_comment = 'Tabla usada para guardar nombres de paises'

    def __str__(self) -> str:
        return self.nombre


class Persona(models.Model):
    p_nombre = models.CharField(
        max_length=45, db_comment='primer nombre de la persona, este campo es obligatorio')
    s_nombre = models.CharField(
        max_length=45, blank=True, null=True, db_comment='segundo nombre de la persona')
    p_apellido = models.CharField(
        max_length=45, db_comment='primer apellido  de la persona, este campo es obligatorio')
    s_apellido = models.CharField(
        max_length=45, blank=True, null=True, db_comment='segundo apellido de la persona')
    genero = models.CharField(
        max_length=9, db_comment='Este campo contiene los generos por los que se puede registrar una persona')
    telefono = models.CharField(
        max_length=45, blank=True, null=True, db_comment='telefono usado para ponerse en contacto con la persona')
    correo = models.CharField(
        max_length=120, db_comment='correo usado para ponerse en contacto con la persona')
    n_identificacion = models.IntegerField(
        db_comment='numero de identificacion de la persona, usado para identificar a una persona a nivel de pais')
    ciudad_residencia = models.ForeignKey(
        Ciudad, models.DO_NOTHING, db_comment='id de la ciudad en la que actualmente esta residiendo la persona')
    ciudad_nacimiento = models.ForeignKey(
        Ciudad, models.DO_NOTHING, related_name='persona_ciudad_nacimiento_set')
    t_identificacion = models.ForeignKey('TIdentificacion', models.DO_NOTHING)
    user = models.OneToOneField(User,null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = True
        db_table = 'persona'
        db_table_comment = 'tabla para guardar los datos de las personas'
        
    def __str__(self) -> str:
        return self.p_nombre

class ProduccionColmena(models.Model):
    idproduccion_colmena = models.AutoField(primary_key=True)
    cant_miel = models.FloatField(blank=True, null=True)
    f_inicio = models.CharField(max_length=45, blank=True, null=True)
    colmena = models.ForeignKey(Colmena, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'produccion_colmena'


class ProduccionEstanque(models.Model):
    idproduccion_colmena = models.AutoField(primary_key=True)
    cant_peces = models.FloatField(blank=True, null=True)
    f_inicio = models.CharField(max_length=45, blank=True, null=True)
    estanque = models.ForeignKey(Estanque, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'produccion_estanque'


class ReporteColmena(models.Model):
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=45)
    infotrata_colmena = models.ForeignKey(InfotrataColmena, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'reporte_colmena'


class ReporteEstanque(models.Model):
    fecha = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=45)
    infotrata_estanque = models.ForeignKey(
        InfotrataEstanque, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'reporte_estanque'


class Sensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)
    tipo_sensor = models.ForeignKey('Tsensor', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sensor'


class TContrato(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_contrato'


class TEmpresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_empresa'


class TIdentificacion(models.Model):
    nombre = models.CharField(
        max_length=45, db_comment='nombre del tipo de identificacion')
    descripcion = models.TextField(
        blank=True, null=True, db_comment='descripcion del tipo de identificacion')

    class Meta:
        managed = True
        db_table = 't_identificacion'
        db_table_comment = 'Tabla para guardar el nombre de los distintos tipos de identificacion, por ejemplo cedula de extranjeria , cedula de ciudadania etc '

    def __str__(self) -> str:
        return self.nombre
    
class Tiptrata(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

    class Meta:
        managed = True
        db_table = 'tiptrata'


class Tratamiento(models.Model):
    fecha_aplicacion = models.DateField()
    dosis = models.FloatField()
    resultado = models.CharField(max_length=250)
    tipo_tratamiento = models.ForeignKey(Tiptrata, models.DO_NOTHING)
    infotrata_colmena = models.ForeignKey(InfotrataColmena, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'tratamiento'


class Tsensor(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'tsensor'
