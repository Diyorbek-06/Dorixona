# Generated by Django 5.1.6 on 2025-03-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar_a', '0002_remove_dori_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dori',
            name='miqdori',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
