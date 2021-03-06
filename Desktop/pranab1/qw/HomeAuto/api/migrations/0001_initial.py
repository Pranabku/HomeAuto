# Generated by Django 4.0.2 on 2022-03-28 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('deviceId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('deviceType', models.CharField(max_length=20)),
                ('lightStatus', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('fanStatus', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
