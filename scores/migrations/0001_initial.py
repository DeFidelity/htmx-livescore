# Generated by Django 3.2.8 on 2021-12-06 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goal', models.PositiveSmallIntegerField(default=0)),
                ('away_goal', models.PositiveSmallIntegerField(default=0)),
                ('game_finished', models.BooleanField(default=False)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='scores.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='scores.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture', to='scores.tournament')),
            ],
        ),
    ]
