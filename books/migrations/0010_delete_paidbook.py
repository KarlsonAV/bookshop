# Generated by Django 3.0.1 on 2021-02-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_paidbook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaidBook',
        ),
    ]