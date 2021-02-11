from django.db import models

# Create your models here.


class User(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=64, verbose_name='사용자명')
    email = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'studying_user'
        verbose_name = "스터딩 사용자"
        verbose_name_plural = '스터딩 사용자'
