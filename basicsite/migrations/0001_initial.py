# Generated by Django 2.0.6 on 2018-06-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userna', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'fb',
            },
        ),
    ]
