# Generated by Django 3.2.9 on 2021-12-03 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20211202_1553'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blogs',
            new_name='post',
        ),
    ]