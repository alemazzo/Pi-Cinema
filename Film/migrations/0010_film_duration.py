# Generated by Django 2.2.7 on 2020-04-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film', '0009_auto_20200405_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.TextField(null=True),
        ),
    ]