# Generated by Django 4.1 on 2023-03-09 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_selection_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='saison',
            field=models.CharField(blank=True, choices=[('été', 'Eté'), ('printemps', 'Printemps'), ('automne', 'Automne'), ('hiver', 'Hiver')], max_length=30, null=True),
        ),
    ]
