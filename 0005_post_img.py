# Generated by Django 3.2.9 on 2021-12-05 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]