# Generated by Django 2.0.3 on 2019-02-23 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_course_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='stdents',
            new_name='students',
        ),
    ]