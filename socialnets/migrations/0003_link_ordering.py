# Generated by Django 2.2.15 on 2020-09-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnets', '0002_auto_20200911_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='ordering',
            field=models.SmallIntegerField(default=0),
        ),
    ]