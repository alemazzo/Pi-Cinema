# Generated by Django 2.2.7 on 2020-04-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film', '0011_auto_20200406_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
