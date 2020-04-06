# Generated by Django 2.2.7 on 2020-04-05 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stagione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SerieTv.Serie')),
            ],
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('videoPath', models.TextField()),
                ('imagePath', models.TextField()),
                ('cachePath', models.TextField(blank=True)),
                ('lastWatch', models.DateTimeField(null=True)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SerieTv.Serie')),
                ('stagione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SerieTv.Stagione')),
            ],
        ),
    ]