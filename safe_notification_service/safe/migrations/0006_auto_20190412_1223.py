# Generated by Django 2.2 on 2019-04-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0005_notificationtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='build_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='device',
            name='bundle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='device',
            name='client',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ANDROID'), (1, 'IOS'), (2, 'EXTENSION')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='version_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
