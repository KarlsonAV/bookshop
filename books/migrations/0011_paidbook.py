# Generated by Django 3.0.1 on 2021-02-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_delete_paidbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_books', models.ManyToManyField(to='books.Book')),
            ],
        ),
    ]
