# Generated by Django 3.0.1 on 2021-02-26 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210226_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can add books!')]},
        ),
    ]
