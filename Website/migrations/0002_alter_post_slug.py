# Generated by Django 5.0.7 on 2024-07-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
