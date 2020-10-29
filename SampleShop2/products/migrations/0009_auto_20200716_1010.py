# Generated by Django 3.0.3 on 2020-07-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200714_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Imagen',
            field=models.ImageField(upload_to='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Tipo',
            field=models.CharField(choices=[('Respirador', 'Protección Respiratoria'), ('Guantes', 'Guantes'), ('Calzado', 'Calzado'), ('Auditivo', 'Protección Auditiva'), ('Visor / Ojos, Cara y Cabza', 'Protección Ojos, Cara y Cabeza'), ('Vestuario', 'Vestuarios'), ('Señalizacion', 'Señalización'), ('Caidas y Ergonomía', 'Ergonomía y Protección de Caídas'), ('Paños', 'Absorbentes y Paños'), ('Primeros Auxilios', 'Primeros Auxilios'), ('Adhesivos, Cintas y Tapes', 'Cintas y Tapes')], max_length=30),
        ),
    ]
