# Generated by Django 3.0.2 on 2020-02-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='title',
            field=models.CharField(max_length=70, verbose_name='Title'),
        ),
    ]
