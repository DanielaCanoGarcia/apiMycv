# Generated by Django 4.2.13 on 2024-12-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_rename_location_header_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='name',
            field=models.TextField(default=''),
        ),
    ]