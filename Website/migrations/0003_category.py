# Generated by Django 5.0.7 on 2024-07-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
