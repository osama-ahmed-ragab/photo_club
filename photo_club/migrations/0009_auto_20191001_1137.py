# Generated by Django 2.2.5 on 2019-10-01 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_club', '0008_auto_20191001_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo',
            new_name='post',
        ),
    ]