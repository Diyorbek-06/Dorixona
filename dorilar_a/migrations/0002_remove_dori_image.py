# Generated by Django 5.1.6 on 2025-03-10 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar_a', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dori',
            name='image',
        ),
    ]
