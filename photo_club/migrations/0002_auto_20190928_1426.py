# Generated by Django 2.2.5 on 2019-09-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]