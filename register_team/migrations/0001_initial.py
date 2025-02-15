# Generated by Django 5.0.7 on 2024-08-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('war_cry', models.CharField(max_length=255)),
                ('foundation_year', models.PositiveIntegerField()),
                ('blots', models.PositiveIntegerField(default=0)),
                ('plifs', models.PositiveIntegerField(default=0)),
                ('advrunghs', models.PositiveIntegerField(default=0)),
                ('total_points', models.PositiveIntegerField(default=50)),
            ],
            options={
                'ordering': ['-total_points'],
            },
        ),
    ]
