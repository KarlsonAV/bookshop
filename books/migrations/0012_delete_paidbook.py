# Generated by Django 3.0.1 on 2021-02-28 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_paidbook'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaidBook',
        ),
    ]