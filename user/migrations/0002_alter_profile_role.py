# Generated by Django 5.0.7 on 2024-08-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN')], max_length=10),
        ),
    ]
