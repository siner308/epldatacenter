# Generated by Django 2.1.5 on 2019-02-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0006_auto_20190201_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_line_5_count',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_line_6_count',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_line_5_count',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_line_6_count',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]