# Generated by Django 4.2.16 on 2024-09-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-05-22'),
            preserve_default=False,
        ),
    ]
