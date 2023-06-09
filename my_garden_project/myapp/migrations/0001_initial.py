# Generated by Django 4.1 on 2023-02-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climat',
            fields=[
                ('id_climat', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'climat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=30, null=True)),
                ('id_climat', models.ForeignKey(blank=True, db_column='id_climat', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.climat')),
            ],
            options={
                'db_table': 'region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_departement', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=30, null=True)),
                ('code', models.CharField(blank=True, max_length=5, null=True)),
                ('id_region', models.ForeignKey(blank=True, db_column='id_region', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.region')),
            ],
            options={
                'db_table': 'departement',
                'managed': True,
            },
        ),
    ]
