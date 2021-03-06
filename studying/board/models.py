from django.db import models

# Create your models here.


class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128, verbose_name='제목', null=True)
    # 텍스트필드는 최대길이설정 필요x
    contents = models.TextField(verbose_name='내용', null=True, default='')
    # 사용자가 탈퇴하면 사용자가 쓴모든글은 삭제 CASCADE
    writer = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='작성자', null=True)
    # auto_now_add:현재시간을 자동으로 추가해주는것
    created_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간', null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'studying_board'
        # fcuser가 아닌 패스트캠퍼스 사용자로 출력하기 위한것
        verbose_name = "스터딩 게시글"
        # plural은 뒤에 복수형으로 나오는걸 방지하기위한것
        verbose_name_plural = '스터딩 게시글'
    
class Photo(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True,null=True)