# Generated by Django 3.2.3 on 2021-05-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='unique_url_id',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
