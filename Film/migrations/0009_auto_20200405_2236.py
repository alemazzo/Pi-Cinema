# Generated by Django 2.2.7 on 2020-04-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Film', '0008_auto_20200405_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='imagePath',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.TextField(null=True),
        ),
    ]
