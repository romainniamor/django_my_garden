# Generated by Django 4.1 on 2023-03-22 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_selection_conseil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conseil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.conseil')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
            ],
            options={
                'db_table': 'collection',
                'managed': True,
            },
        ),
    ]