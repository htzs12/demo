# Generated by Django 2.0.5 on 2018-12-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_register', '0002_auto_20181207_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
