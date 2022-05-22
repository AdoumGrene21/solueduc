# Generated by Django 3.2.8 on 2022-05-22 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=120, verbose_name='Nom Cours')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=120, verbose_name='Nom salle')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=200, verbose_name='Prenoms')),
                ('sexe', models.CharField(max_length=120, verbose_name='Sexe')),
                ('address', models.CharField(max_length=220)),
                ('nationalite', models.CharField(max_length=120)),
                ('cours', models.ManyToManyField(to='ressource.Cours')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ressource.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, verbose_name='nom')),
                ('prenoms', models.CharField(max_length=20, verbose_name='prenom')),
                ('sexe', models.CharField(max_length=120, verbose_name='sexe')),
                ('specialite', models.CharField(max_length=120, verbose_name='specialite')),
                ('cours', models.ManyToManyField(to='ressource.Cours')),
            ],
        ),
    ]
