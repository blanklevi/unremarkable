# Generated by Django 2.2 on 2020-07-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20200714_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default='Hello this is the details'),
            preserve_default=False,
        ),
    ]
