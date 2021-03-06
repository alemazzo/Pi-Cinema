# Generated by Django 2.2.7 on 2020-04-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.TextField()),
                ('duration', models.TextField()),
                ('videoPath', models.TextField()),
                ('imagePath', models.TextField()),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
            },
        ),
    ]
