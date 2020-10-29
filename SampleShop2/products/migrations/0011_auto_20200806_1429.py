# Generated by Django 3.0.3 on 2020-08-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200728_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contactos',
        ),
        migrations.AddField(
            model_name='product',
            name='Unidades',
            field=models.CharField(choices=[('PAR', 'Par'), ('PQT', 'Paquete'), ('PQT8', 'Paquete de 8'), ('PZA', 'Pieza'), ('CJTA100', 'Cajita de 100'), ('CJTA50', 'Cajita de 50'), ('CONJ', 'Conjunto'), ('ROLL', 'Roll'), ('TB', 'Tb')], default='PZA', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Tipo',
            field=models.CharField(choices=[('Respirador', 'Protección Respiratoria'), ('Guantes', 'Guantes'), ('Calzado', 'Calzado'), ('Auditivo', 'Protección Auditiva'), ('Visor/Ojos, Cara y Cabeza', 'Protección Ojos, Cara y Cabeza'), ('Vestuario', 'Vestuarios'), ('Señalizacion', 'Señalización'), ('Caidas/Ergonomía', 'Ergonomía y Protección de Caídas'), ('Paños', 'Absorbentes y Paños'), ('Primeros Auxilios', 'Primeros Auxilios'), ('Adhesivos, Cintas y Tapes', 'Cintas y Tapes')], default='PZA', max_length=30),
        ),
    ]