# Generated by Django 5.0.3 on 2024-03-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_alter_content_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
