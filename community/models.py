from django.contrib.auth.models import User
from django.db import models


# 카테고리 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/community/category/{self.slug}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):   # 포스트 모델
    title = models.CharField(max_length=200)    # 제목: Char필드는 제한필요(최대=한글100자)
    content = models.TextField()                # 내용
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이: FK, User모델에서 가져옴 삭제연동
    create_date = models.DateTimeField(auto_now_add=True)       # 생성일: 최초 생성시 자동생성, 수정시 변경안됨
    modify_date = models.DateTimeField(null=True, blank=True)   # 수정일: 수동생성(null, 공백 가능)
    views = models.IntegerField(default=0)      # 조회수
    likes = models.IntegerField(default=0)      # 좋아요
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    attach = models.ImageField(upload_to='community/images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.title   # Post를 식별할 상황에서 기본인 id가 아니라 title값을 불러와줘서 알아보기 쉽게 함
