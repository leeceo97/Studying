# Generated by Django 3.1.6 on 2021-02-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20210219_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='modified_dttm',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_dttm',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.CharField(default='', max_length=150, verbose_name='댓글'),
        ),
    ]