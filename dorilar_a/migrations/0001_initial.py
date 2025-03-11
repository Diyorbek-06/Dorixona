# Generated by Django 5.1.6 on 2025-03-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('nomi', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('xususiyat', models.TextField()),
                ('chiqarilgan_vaqt', models.DateField(auto_now_add=True)),
                ('tugash_muddati', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='dori_images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Dori',
                'ordering': ['-create_at'],
            },
        ),
    ]
