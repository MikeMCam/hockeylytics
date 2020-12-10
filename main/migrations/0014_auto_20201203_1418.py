# Generated by Django 3.1.2 on 2020-12-03 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_auto_20201203_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerlist',
            name='dummy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.dummy'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='dummy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.dummy'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]