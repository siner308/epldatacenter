# Generated by Django 2.1.5 on 2019-02-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0003_auto_20190131_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='home_team_defender_count',
            new_name='home_team_line_1_count',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='home_team_midfielder_count',
            new_name='home_team_line_2_count',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='home_team_forward_count',
            new_name='home_team_line_3_count',
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_line_4_count',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
