# Generated by Django 4.2.2 on 2023-07-05 05:01

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255, verbose_name='Nombre de la Compania')),
                ('ruc', models.CharField(max_length=255, verbose_name='RUC de la Compania')),
                ('supervisor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Supervisor de la Compania')),
                ('encargado', models.CharField(blank=True, max_length=255, null=True, verbose_name='Encargado de la Compania')),
                ('planillero', models.CharField(blank=True, max_length=255, null=True, verbose_name='Planillero de la Compania')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': 'empresas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaUnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propuesta', models.FileField(blank=True, null=True, upload_to='evidencia-unica/', verbose_name='Propuesta del Servicio')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha de Firma')),
                ('desvinculacion', models.FileField(blank=True, null=True, upload_to='evidencia-unica/', verbose_name='Desvinculacion')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaUnica',
                'verbose_name_plural': 'EvidenciasUnicas',
                'db_table': 'evidencia_unica',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaMensualRC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Enero')),
                ('febrero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Febrero')),
                ('marzo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Marzo')),
                ('abril', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Abril')),
                ('mayo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Mayo')),
                ('junio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Junio')),
                ('julio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Julio')),
                ('agosto', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Agosto')),
                ('septiembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Septiembre')),
                ('octubre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Octubre')),
                ('noviembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Noviembre')),
                ('diciembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualRC/', verbose_name='Diciembre')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaMensualRC',
                'verbose_name_plural': 'EvidenciasMensualesRC',
                'db_table': 'evidencia_mensual_rc',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaMensualPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Enero')),
                ('febrero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Febrero')),
                ('marzo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Marzo')),
                ('abril', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Abril')),
                ('mayo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Mayo')),
                ('junio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Junio')),
                ('julio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Julio')),
                ('agosto', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Agosto')),
                ('septiembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Septiembre')),
                ('octubre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Octubre')),
                ('noviembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Noviembre')),
                ('diciembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualPI/', verbose_name='Diciembre')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaMensualPI',
                'verbose_name_plural': 'EvidenciasMensualesPI',
                'db_table': 'evidencia_mensual_pi',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaMensualI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Enero')),
                ('febrero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Febrero')),
                ('marzo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Marzo')),
                ('abril', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Abril')),
                ('mayo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Mayo')),
                ('junio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Junio')),
                ('julio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Julio')),
                ('agosto', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Agosto')),
                ('septiembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Septiembre')),
                ('octubre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Octubre')),
                ('noviembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Noviembre')),
                ('diciembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualI/', verbose_name='Diciembre')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaMensualImpuesto',
                'verbose_name_plural': 'EvidenciasMensualesImpuestos',
                'db_table': 'evidencia_mensual_i',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaMensualEF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Enero')),
                ('febrero', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Febrero')),
                ('marzo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Marzo')),
                ('abril', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Abril')),
                ('mayo', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Mayo')),
                ('junio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Junio')),
                ('julio', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Julio')),
                ('agosto', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Agosto')),
                ('septiembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Septiembre')),
                ('octubre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Octubre')),
                ('noviembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Noviembre')),
                ('diciembre', models.FileField(blank=True, null=True, upload_to='evidencia-mensualEF/', verbose_name='Diciembre')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaMensualEF',
                'verbose_name_plural': 'EvidenciasMensualesEF',
                'db_table': 'evidencia_mensual_ef',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaAnual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidencia_comunicacion', models.FileField(blank=True, null=True, upload_to='evidencia-anual/', verbose_name='Evidencia de la comunicacion')),
                ('evidencia_presentacion', models.FileField(blank=True, null=True, upload_to='evidencia-anual/', verbose_name='Evidencia de la presentacion')),
                ('evidencia_startup', models.FileField(blank=True, null=True, upload_to='evidencia-anual/', verbose_name='Evidencia Start Up')),
                ('evidencia_eeff', models.FileField(blank=True, null=True, upload_to='evidencia-anual/', verbose_name='Evidencia de EEFF')),
                ('evidencia_dja', models.FileField(blank=True, null=True, upload_to='evidencia-anual/', verbose_name='Evidencia de DJA')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.empresa')),
            ],
            options={
                'verbose_name': 'EvidenciaAnual',
                'verbose_name_plural': 'EvidenciasAnual',
                'db_table': 'evidencia_anual',
                'ordering': ['id'],
            },
        ),
    ]
