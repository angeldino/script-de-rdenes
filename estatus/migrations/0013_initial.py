# Generated by Django 5.0.6 on 2024-08-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estatus', '0012_remove_createorder_cliente_delete_createuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='newTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(blank=True, default='Colocar orden', max_length=255, null=True)),
                ('trailer', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('remolque', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('posicion', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('destino', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('distancia', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('tiempo_estimado', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
