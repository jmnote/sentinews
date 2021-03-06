# Generated by Django 3.2.4 on 2021-06-15 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=80, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_ip', models.CharField(max_length=32)),
                ('content', models.CharField(max_length=10000)),
                ('comments', models.CharField(max_length=1000)),
                ('comments_count', models.IntegerField()),
                ('polarities', models.CharField(max_length=64)),
                ('avg_polarity', models.FloatField()),
            ],
        ),
    ]
