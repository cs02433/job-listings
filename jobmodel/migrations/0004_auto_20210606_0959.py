# Generated by Django 3.2.3 on 2021-06-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobmodel', '0003_auto_20210529_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='exam',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='exam_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
