# Generated by Django 4.0.4 on 2022-05-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('couleur', models.CharField(max_length=42)),
                ('modele', models.CharField(max_length=100)),
                ('annee', models.IntegerField(max_length=5)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
