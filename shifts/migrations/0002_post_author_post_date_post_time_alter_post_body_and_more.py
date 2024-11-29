# Generated by Django 5.1.3 on 2024-11-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='不明', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]