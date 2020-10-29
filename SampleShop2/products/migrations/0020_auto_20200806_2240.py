# Generated by Django 3.0.3 on 2020-08-07 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200806_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Tipo',
            field=models.CharField(choices=[('respiratoria', 'Protección Respiratoria'), ('guantes', 'Guantes'), ('calzado', 'Calzado'), ('auditiva', 'Protección Auditiva'), ('cabeza', 'Protección Ojos, Cara y Cabeza'), ('vestuario', 'Vestuario'), ('señalizacion', 'Señalización'), ('ergonomía y Protección de Caídas', 'Ergonomía y Protección de Caídas'), ('absorbentes y Paños', 'Absorbentes y Paños'), ('auxilios', 'Primeros Auxilios'), ('adhesivos', 'Adhesivos, Cintas y Tapes')], max_length=50),
        ),
    ]
