# Generated by Django 3.1.6 on 2021-02-25 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20210225_0136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='post',
            new_name='board',
        ),
    ]
