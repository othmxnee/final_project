# Generated by Django 4.1.3 on 2024-05-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matricule',
            field=models.CharField(max_length=50),
        ),
    ]
