# Generated by Django 3.1.6 on 2021-02-06 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True, verbose_name='제목')),
                ('contents', models.TextField(default='', null=True, verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '스터딩 게시글',
                'verbose_name_plural': '스터딩 게시글',
                'db_table': 'studying_board',
            },
        ),
    ]
