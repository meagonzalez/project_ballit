# Generated by Django 5.0.7 on 2024-08-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_championship', '0006_alter_match_round_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='teams',
            field=models.ManyToManyField(related_name='championships', to='start_championship.team'),
        ),
    ]
