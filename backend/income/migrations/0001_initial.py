# Generated by Django 4.1 on 2023-01-06 02:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=0, max_digits=7)),
                ('date', models.DateTimeField(auto_now=True)),
                ('memo', models.CharField(max_length=20)),
                ('purpose', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BinaryField(default=b'\x08')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'income',
            },
        ),
    ]
