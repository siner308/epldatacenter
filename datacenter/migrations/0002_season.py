# Generated by Django 2.1.5 on 2019-01-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(blank=True, max_length=100)),
                ('html', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]