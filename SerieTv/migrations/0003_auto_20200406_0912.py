# Generated by Django 2.2.7 on 2020-04-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SerieTv', '0002_auto_20200405_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episodio',
            name='numero',
        ),
        migrations.AddField(
            model_name='episodio',
            name='titolo',
            field=models.TextField(null=True),
        ),
    ]
