# Generated by Django 4.2.8 on 2024-01-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_swimposts_author_swimposts_swim_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimposts',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='swimposts',
            name='location',
            field=models.TextField(max_length=300),
        ),
    ]
