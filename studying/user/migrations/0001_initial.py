# Generated by Django 3.1.6 on 2021-02-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('useremail', models.EmailField(max_length=128, verbose_name='사용자이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '스터딩 사용자',
                'verbose_name_plural': '스터딩 사용자',
                'db_table': 'studying_user',
            },
        ),
    ]
