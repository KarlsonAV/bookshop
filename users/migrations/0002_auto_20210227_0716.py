# Generated by Django 3.0.1 on 2021-02-27 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('chek', 'heck')]},
        ),
    ]
