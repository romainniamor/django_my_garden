# Generated by Django 4.1 on 2023-03-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_produit_besoin_eau_alter_produit_besoin_soleil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile'),
        ),
    ]