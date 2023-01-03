# Generated by Django 4.1 on 2023-01-03 08:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.BinaryField(max_length=60)),
                ('salt', models.BinaryField(max_length=29)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
