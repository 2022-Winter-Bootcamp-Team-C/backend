# Generated by Django 4.1 on 2023-01-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]