# Generated by Django 5.1.1 on 2024-09-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardProduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='timezone',
            field=models.DateField(),
        ),
    ]