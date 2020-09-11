# Generated by Django 2.2.14 on 2020-09-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200911_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s3_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s3_gender',
            field=models.CharField(blank=True, default='X', max_length=1),
        ),
    ]
