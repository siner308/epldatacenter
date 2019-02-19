# Generated by Django 2.1.5 on 2019-02-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0014_auto_20190204_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_avg_conceded',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_avg_goal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_change_created',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_clean_sheet',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_drawn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_lost',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='away_won',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_avg_conceded',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_avg_goal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_change_created',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_clean_sheet',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_drawn',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_lost',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='home_won',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]