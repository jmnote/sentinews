# Generated by Django 3.2.4 on 2021-06-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_article_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='polarity',
        ),
        migrations.AddField(
            model_name='article',
            name='avg_polarity',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='polarities',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
