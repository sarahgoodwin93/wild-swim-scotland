# Generated by Django 4.2.8 on 2024-01-29 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_joinswim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
    ]
