# Generated by Django 4.1 on 2023-03-20 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_planning_date_fin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Astuce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=100, null=True)),
                ('contenu', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.produit')),
            ],
            options={
                'db_table': 'astuce',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='selection',
            name='astuces',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.astuce'),
        ),
    ]
