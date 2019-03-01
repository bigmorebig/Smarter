# Generated by Django 2.0.3 on 2019-02-27 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0014_auto_20190227_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='courses',
            new_name='course_nums',
        ),
        migrations.RenameField(
            model_name='courseorg',
            old_name='fav_num',
            new_name='fav_nums',
        ),
        migrations.RemoveField(
            model_name='courseorg',
            name='categroy',
        ),
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='国内名校', max_length=10, verbose_name='机构标签'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='Logo'),
        ),
    ]