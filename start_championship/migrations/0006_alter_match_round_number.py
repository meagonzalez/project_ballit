# Generated by Django 5.0.7 on 2024-08-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_championship', '0005_team_remove_championship_current_phase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='round_number',
            field=models.IntegerField(default=0),
        ),
    ]
