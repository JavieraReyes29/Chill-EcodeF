# Generated by Django 3.2.19 on 2023-05-26 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestioncliente', '0002_auto_20230508_2116'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioncliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('orden_cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cotizacion.cotizacion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producto')),
            ],
        ),
    ]
