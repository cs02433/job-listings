# Generated by Django 3.2.3 on 2021-07-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmodel', '0007_auto_20210703_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='logo_url',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]