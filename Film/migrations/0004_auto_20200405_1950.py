# Generated by Django 2.2.7 on 2020-04-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film', '0003_film_cachepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='cachePath',
            field=models.TextField(blank=True),
        ),
    ]
