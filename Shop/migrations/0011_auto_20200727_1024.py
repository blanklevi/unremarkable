# Generated by Django 2.2 on 2020-07-27 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Size',
            new_name='ProductSize',
        ),
    ]
