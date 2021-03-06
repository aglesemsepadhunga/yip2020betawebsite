# Generated by Django 2.2.14 on 2020-09-06 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('discord_id', models.TextField(blank=True, null=True)),
                ('zoom_id', models.TextField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
