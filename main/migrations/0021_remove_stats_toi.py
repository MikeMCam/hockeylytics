# Generated by Django 3.1.2 on 2020-12-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_match_createdby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='toi',
        ),
    ]
