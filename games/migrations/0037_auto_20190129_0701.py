# Generated by Django 2.0.5 on 2019-01-29 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0036_auto_20181208_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Featured',
        ),
    ]
