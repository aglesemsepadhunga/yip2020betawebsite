# Generated by Django 3.1.2 on 2020-11-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200911_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedteaminfo',
            name='publi',
            field=models.IntegerField(default=0),
        ),
    ]
