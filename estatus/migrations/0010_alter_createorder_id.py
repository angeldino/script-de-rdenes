# Generated by Django 5.0.6 on 2024-08-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estatus', '0009_createorder_fecha_previo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createorder',
            name='id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
