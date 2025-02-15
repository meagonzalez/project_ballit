# Generated by Django 5.0.7 on 2024-08-04 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_team', '0001_initial'),
        ('start_championship', '0008_alter_match_team_a_alter_match_winner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='round',
        ),
        migrations.RemoveField(
            model_name='championship',
            name='name',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score_a',
        ),
        migrations.RemoveField(
            model_name='match',
            name='score_b',
        ),
        migrations.AddField(
            model_name='championship',
            name='started',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='match',
            name='championship',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='start_championship.championship'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='phase',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_a', to='register_team.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_b', to='register_team.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_wins', to='register_team.team'),
        ),
        migrations.DeleteModel(
            name='Round',
        ),
    ]
