# Generated by Django 4.1 on 2023-03-22 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selection',
            name='conseil',
        ),
    ]