# Generated by Django 2.0.5 on 2018-12-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('birthday', models.DateField(verbose_name='生日')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('width', models.FloatField()),
                ('height', models.IntegerField()),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
