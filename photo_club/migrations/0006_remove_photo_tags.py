# Generated by Django 2.2.5 on 2019-10-01 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_club', '0005_auto_20191001_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
    ]
