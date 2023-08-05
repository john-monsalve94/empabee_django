# Generated by Django 4.2.1 on 2023-08-05 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_rename_nombre_infotrataestanque_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='infotrata_colmena',
        ),
        migrations.AddField(
            model_name='infotratacolmena',
            name='tratamiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='principal.tratamiento'),
            preserve_default=False,
        ),
    ]