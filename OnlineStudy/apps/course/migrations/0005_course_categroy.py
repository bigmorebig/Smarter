# Generated by Django 2.0.3 on 2019-02-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20190223_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='categroy',
            field=models.CharField(default='后端开发', max_length=20, verbose_name='课程类别'),
        ),
    ]