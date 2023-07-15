# Generated by Django 4.2.2 on 2023-07-15 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabezaFactura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cabeza_facturacol', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cabeza_factura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre de la ciudad', max_length=45)),
                ('codigo', models.IntegerField(db_comment='codigo de la ciudad')),
                ('c_postal', models.IntegerField(blank=True, db_comment='codigo postal de la ciudad', null=True)),
            ],
            options={
                'db_table': 'ciudad',
                'db_table_comment': 'Tabla utilizada para guardar nombres ,codigos postales y codigos de ciudad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Colmena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='Nombre: Este campo almacena el nombre o identificacin de un registro especfico relacionado con la apicultura. Puede ser el nombre de un apicultor, una granja de abejas o cualquier otro nombre que ayude a identificar la entrada en la base de datos.', max_length=45)),
                ('feinicio', models.DateField(db_comment='Fecha inicio: Este campo registra la fecha en la que comenz un evento o perodo relevante para la apicultura. Puede representar la fecha de inicio de una temporada de cosecha, el inicio de un proyecto especfico o cualquier otro evento relacionado con la apicultura.')),
                ('fefin', models.DateField(db_comment='Fecha final: Este campo almacena la fecha en la que termina un evento o perodo relacionado con la apicultura. Puede ser la fecha de finalizacin de una temporada de cosecha, el final de un proyecto especfico o cualquier otro evento relevante.')),
                ('especies', models.CharField(db_comment='Especies: Este campo registra las especies de abejas presentes en una ubicacin especfica. Puede incluir diferentes tipos de abejas, como Apis mellifera (abeja de la miel).\nApis mellifera: tambin conocida como abeja de la miel europea, es la especie de abeja melfera ms comnmente utilizada en la apicultura a nivel mundial.\nApis cerana: una especie de abeja melfera nativa de Asia, tambin utilizada en la apicultura en algunas regiones.\nApis dorsata: conocida como abeja gigante, es una especie de abeja melfera que se encuentra en el sudeste asitico y algunas partes de la India.\nApis florea: una especie de abeja melfera ms pequea que se encuentra en regiones de Asia y frica.\nApis andreniformis: otra especie de abeja melfera nativa de Asia.', max_length=225)),
                ('polifloracion', models.CharField(db_comment='Poli floracin: Este campo indica si hay poli floracin en la ubicacin o evento relacionado con la apicultura. La poli floracin se refiere a la presencia de mltiples especies de flores o plantas que proporcionan nctar y polen a las abejas. Puede ser un factor importante para el xito y la productividad de las colmenas.', max_length=225)),
            ],
            options={
                'db_table': 'colmena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feinicio', models.DateField()),
                ('fefinal', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pago', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'contrato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cultivo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'cultivo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=45)),
                ('carrera', models.CharField(blank=True, max_length=45, null=True)),
                ('numero', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('ciudad_departamentos_id', models.IntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.ciudad')),
            ],
            options={
                'db_table': 'direccion',
                'db_table_comment': 'esta tabla guarda las direcciones donde puedes encontrar una empresa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EspecieAbeja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'especie_abeja',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EspeciePez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'especie_pez',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('feinicio', models.DateField()),
                ('fefinal', models.DateField()),
                ('especies', models.CharField(max_length=150)),
                ('cantpeces', models.IntegerField()),
                ('alimentacion', models.CharField(max_length=150)),
                ('frecualimentacion', models.CharField(max_length=150)),
                ('tiemcultivo', models.IntegerField()),
                ('cultivo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cultivo')),
                ('especie_pez', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.especiepez')),
            ],
            options={
                'db_table': 'estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InfotrataColmena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('f_inicio', models.DateField()),
                ('f_fin', models.DateField(blank=True, null=True)),
                ('infotrata_colmenacol', models.IntegerField(blank=True, null=True)),
                ('colmena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.colmena')),
            ],
            options={
                'db_table': 'infotrata_colmena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InfotrataEstanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('f_inicio', models.DateField()),
                ('f_fin', models.DateField()),
                ('estanque_id', models.IntegerField()),
                ('estanque_id1', models.ForeignKey(db_column='estanque_id1', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.estanque')),
            ],
            options={
                'db_table': 'infotrata_estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del pais', max_length=45)),
                ('codigo', models.IntegerField(db_comment='Codigo del pais')),
            ],
            options={
                'db_table': 'pais',
                'db_table_comment': 'Tabla usada para guardar nombres de paises',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TContrato',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('desc', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 't_contrato',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TEmpresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('desc', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 't_empresa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TIdentificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del tipo de identificacion', max_length=45)),
                ('descripcion', models.TextField(blank=True, db_comment='descripcion del tipo de identificacion', null=True)),
            ],
            options={
                'db_table': 't_identificacion',
                'db_table_comment': 'Tabla para guardar el nombre de los distintos tipos de identificacion, por ejemplo cedula de extranjeria , cedula de ciudadania etc ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tiptrata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'tiptrata',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tsensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'tsensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aplicacion', models.DateField()),
                ('dosis', models.FloatField()),
                ('resultado', models.CharField(max_length=250)),
                ('infotrata_colmena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.infotratacolmena')),
                ('tipo_tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tiptrata')),
            ],
            options={
                'db_table': 'tratamiento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=150)),
                ('ubicacion', models.CharField(max_length=150)),
                ('tipo_sensor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tsensor')),
            ],
            options={
                'db_table': 'sensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReporteEstanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=45)),
                ('infotrata_estanque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.infotrataestanque')),
            ],
            options={
                'db_table': 'reporte_estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReporteColmena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=45)),
                ('infotrata_colmena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.infotratacolmena')),
            ],
            options={
                'db_table': 'reporte_colmena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProduccionEstanque',
            fields=[
                ('idproduccion_colmena', models.AutoField(primary_key=True, serialize=False)),
                ('cant_peces', models.FloatField(blank=True, null=True)),
                ('f_inicio', models.CharField(blank=True, max_length=45, null=True)),
                ('estanque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.estanque')),
            ],
            options={
                'db_table': 'produccion_estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProduccionColmena',
            fields=[
                ('idproduccion_colmena', models.AutoField(primary_key=True, serialize=False)),
                ('cant_miel', models.FloatField(blank=True, null=True)),
                ('f_inicio', models.CharField(blank=True, max_length=45, null=True)),
                ('colmena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.colmena')),
            ],
            options={
                'db_table': 'produccion_colmena',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nombre', models.CharField(db_comment='primer nombre de la persona, este campo es obligatorio', max_length=45)),
                ('s_nombre', models.CharField(blank=True, db_comment='segundo nombre de la persona', max_length=45, null=True)),
                ('p_apellido', models.CharField(db_comment='primer apellido  de la persona, este campo es obligatorio', max_length=45)),
                ('s_apellido', models.CharField(blank=True, db_comment='segundo apellido de la persona', max_length=45, null=True)),
                ('genero', models.CharField(db_comment='Este campo contiene los generos por los que se puede registrar una persona', max_length=9)),
                ('telefono', models.IntegerField(db_comment='telefono usado para ponerse en contacto con la persona')),
                ('correo', models.CharField(db_comment='correo usado para ponerse en contacto con la persona', max_length=120)),
                ('n_identificacion', models.IntegerField(db_comment='numero de identificacion de la persona, usado para identificar a una persona a nivel de pais')),
                ('ciudad_nacimiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='persona_ciudad_nacimiento_set', to='principal.ciudad')),
                ('ciudad_residencia', models.ForeignKey(db_comment='id de la ciudad en la que actualmente esta residiendo la persona', on_delete=django.db.models.deletion.DO_NOTHING, to='principal.ciudad')),
                ('t_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tidentificacion')),
            ],
            options={
                'db_table': 'persona',
                'db_table_comment': 'tabla para guardar los datos de las personas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MSensorEstanque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechahora', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estanque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.estanque')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.sensor')),
            ],
            options={
                'db_table': 'm_sensor_estanque',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MSensorColmena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechahora', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('colmena', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.colmena')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.sensor')),
            ],
            options={
                'db_table': 'm_sensor_colmena',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='infotrataestanque',
            name='tratamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tratamiento'),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('nit', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.direccion')),
                ('t_empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tempresa')),
            ],
            options={
                'db_table': 'empresa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_comment='nombre del departamento', max_length=45)),
                ('codigo', models.IntegerField(db_comment='codigo del departamento')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.pais')),
            ],
            options={
                'db_table': 'departamentos',
                'db_table_comment': 'Tabla usada para guardar nombres de departamentos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CuerpoFactura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cabeza_factura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cabezafactura')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.contrato')),
            ],
            options={
                'db_table': 'cuerpo_factura',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='cultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cultivo'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='t_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tcontrato'),
        ),
        migrations.AddField(
            model_name='colmena',
            name='cultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.cultivo'),
        ),
        migrations.AddField(
            model_name='colmena',
            name='especie_abeja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.especieabeja'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.departamentos'),
        ),
        migrations.AddField(
            model_name='cabezafactura',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.empresa'),
        ),
        migrations.CreateModel(
            name='AsignacionEncargado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_inicial', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_final', models.CharField(blank=True, max_length=45, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.empresa')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='principal.persona')),
            ],
            options={
                'db_table': 'asignacion_encargado',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='infotrataestanque',
            unique_together={('id', 'estanque_id')},
        ),
    ]
