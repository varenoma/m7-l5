# Generated by Django 5.2.1 on 2025-05-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
