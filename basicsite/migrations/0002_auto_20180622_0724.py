# Generated by Django 2.0.6 on 2018-06-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]