from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.
# Blog TB
# 블로그 기본키, 회원 기본키, 블로그 카테고리 기본키, 제목, 내용, 조회수 
# 추천수, 비추천수, 등록날짜, 수정날짜
class Post(models.Model):
    title = models.CharField(max_length=200, help_text="블로그 제목")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="블로그 사용자")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    content = models.TextField(help_text="블로그 내용")
    image = models.ImageField(blank=True, null=True, help_text="블로그 이미지")
    view_count = models.IntegerField(default=0, help_text="블로그 조회수")
    likes_user = models.ManyToManyField(User, blank=True, related_name='likes_user')
    create_date = models.DateField(auto_now_add=True, help_text="블로그 게시물 생성일")
    update_date = models.DateField(auto_now=True, help_text="블로그 게시물 수정일")

    class Meta:
        ordering = ['-create_date']
    
    def __str__(self):
        return '%s - %s' %(self.id, self.title)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    @property
    def update_view_count(self):
        self.view_count = self.view_count + 1
        self.save()

    def count_likes_user(self):
        return self.likes_user.count()

class Category(models.Model):
    name = models.CharField(max_length=30, help_text="블로그 카테고리") 

    def __str__(self):
        return self.name

