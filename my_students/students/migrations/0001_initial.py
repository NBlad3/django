# Generated by Django 5.2 on 2025-05-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('birthdate', models.CharField(max_length=255)),
            ],
        ),
    ]
