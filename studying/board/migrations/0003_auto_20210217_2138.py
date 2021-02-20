# Generated by Django 3.1.6 on 2021-02-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_board_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='registered_dttm',
            new_name='created_dttm',
        ),
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(default='', upload_to='timeline_photo/%Y/%m'),
        ),
    ]