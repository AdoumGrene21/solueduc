# Generated by Django 3.2.8 on 2022-05-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource', '0003_auto_20220522_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]