# Generated by Django 3.2.8 on 2022-05-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource', '0007_cours_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
