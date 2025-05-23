# Generated by Django 5.2.1 on 2025-05-23 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0003_alter_moviemodel_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie.moviemodel')),
            ],
        ),
    ]
