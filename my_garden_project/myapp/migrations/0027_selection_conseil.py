# Generated by Django 4.1 on 2023-03-22 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_conseil_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='conseil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.conseil'),
        ),
    ]
