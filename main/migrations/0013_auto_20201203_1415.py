# Generated by Django 3.1.2 on 2020-12-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201203_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerlist',
            name='leave_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]