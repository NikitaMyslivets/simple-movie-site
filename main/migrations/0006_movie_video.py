# Generated by Django 3.1.3 on 2020-11-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FilePathField(default=None, null=True),
        ),
    ]
