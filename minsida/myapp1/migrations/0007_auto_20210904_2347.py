# Generated by Django 3.1.5 on 2021-09-04 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_auto_20210824_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulistan',
            name='arbetsorder',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='pulistan',
            name='objektid',
            field=models.TextField(default='', max_length=500),
        ),
    ]