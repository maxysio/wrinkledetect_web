# Generated by Django 3.0.7 on 2020-08-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrinkledetect', '0005_auto_20200807_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageanalysis',
            name='num_objects',
            field=models.IntegerField(default=0, verbose_name='Number of Wrinkles: '),
        ),
    ]
