# Generated by Django 3.0.4 on 2020-03-24 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200324_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='summary',
        ),
    ]
