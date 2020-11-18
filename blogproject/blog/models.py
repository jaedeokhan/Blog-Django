from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
# Blog TB
# 블로그 기본키, 회원 기본키, 블로그 카테고리 기본키, 제목, 내용, 조회수, 
# 추천수, 비추천수, 등록날짜, 수정날짜
class Blog(models.Model):
    title = models.CharField(max_length=200, help_text="블로그 제목")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="블로그 사용자")
    category = models.CharField(max_length=30, help_text="블로그 카테고리") 
    content = models.TextField(help_text="블로그 내용")
    view_count = models.IntegerField(default=0, help_text="블로그 조회수")
    like_count = models.IntegerField(default=0, help_text="블로그 추천수")
    dislike_count = models.IntegerField(default=0, help_text="블로그 비추천수")
    create_date = models.DateField(auto_now_add=True, help_text="블로그 게시물 생성일")
    update_date = models.DateField(auto_now=True, help_text="블로그 게시물 수정일")

    def __str__(self):
        return self.title

