# Generated by Django 2.2.14 on 2020-09-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200911_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='num_of_students',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s1_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='s2_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='teacher_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='teacher_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='extendedteaminfo',
            name='teacher_phone_num',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
