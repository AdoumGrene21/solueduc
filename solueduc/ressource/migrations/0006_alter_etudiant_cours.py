# Generated by Django 3.2.8 on 2022-05-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource', '0005_alter_etudiant_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='cours',
            field=models.ManyToManyField(blank=True, null=True, to='ressource.Cours'),
        ),
    ]
