# Generated by Django 3.1.6 on 2021-02-08 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='useremail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]
