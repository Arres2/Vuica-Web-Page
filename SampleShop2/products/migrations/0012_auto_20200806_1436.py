# Generated by Django 3.0.3 on 2020-08-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200806_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Tipo',
            field=models.CharField(choices=[('Respirador', 'Protección Respiratoria'), ('Guantes', 'Guantes'), ('Calzado', 'Calzado'), ('Auditivo', 'Protección Auditiva'), ('Visor/Ojos, Cara y Cabeza', 'Protección Ojos, Cara y Cabeza'), ('Vestuario', 'Vestuarios'), ('Señalizacion', 'Señalización'), ('Caidas/Ergonomía', 'Ergonomía y Protección de Caídas'), ('Paños', 'Absorbentes y Paños'), ('Primeros Auxilios', 'Primeros Auxilios'), ('Adhesivos, Cintas y Tapes', 'Cintas y Tapes')], max_length=30),
        ),
    ]
