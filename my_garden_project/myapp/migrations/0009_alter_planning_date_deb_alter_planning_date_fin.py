# Generated by Django 4.1 on 2023-03-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_id_climat_planning_climat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date_deb',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='planning',
            name='date_fin',
            field=models.DateField(blank=True, max_length=5, null=True),
        ),
    ]