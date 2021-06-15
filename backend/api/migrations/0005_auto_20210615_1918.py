# Generated by Django 3.2.4 on 2021-06-15 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210615_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
        migrations.AddField(
            model_name='article',
            name='comments_count',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='avg_polarity',
            field=models.FloatField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='comments',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='article',
            name='polarities',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='user_ip',
            field=models.CharField(default=2, max_length=32),
            preserve_default=False,
        ),
    ]