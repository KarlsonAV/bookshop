# Generated by Django 3.0.1 on 2021-02-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210227_0716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='paid_books',
            field=models.ManyToManyField(blank=True, null=True, to='books.Book'),
        ),
    ]
