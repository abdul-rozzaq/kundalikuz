# Generated by Django 5.0.3 on 2024-03-21 19:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_day_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]