# Generated by Django 5.1.3 on 2024-11-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0007_remove_post_time_post_endtime_post_starttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='substitute',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
