# Generated by Django 4.1.3 on 2022-11-28 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instsite', '0003_hashes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hashes',
        ),
    ]