# Django Blog 프로젝트
> Python의 프레임워크인 Django를 이용한 개인 블로그 팀 프로젝트입니다.
> 
> 배포는 pythonanywhere를 통해 배포했습니다 => <a href="http://hjaedeok.pythonanywhere.com/" target="_blank">사이트 바로가기</a> 
## 바로가기
1. [제작 기간 & 참여 인원](https://github.com/jaedeokhan/python-django-blog/blob/main/README.md#1-%EC%A0%9C%EC%9E%91-%EA%B8%B0%EA%B0%84--%EC%B0%B8%EC%97%AC-%EC%9D%B8%EC%9B%90)
2. [사용 기술](https://github.com/jaedeokhan/python-django-blog/blob/main/README.md#2-%EC%82%AC%EC%9A%A9-%EA%B8%B0%EC%88%A0)
3. [ERD 설계](https://github.com/jaedeokhan/python-django-blog/blob/main/README.md#3-erd-%EC%84%A4%EA%B3%84)
4. [기능](https://github.com/jaedeokhan/python-django-blog/blob/main/README.md#4-%EA%B8%B0%EB%8A%A5)

## 1. 제작 기간 & 참여 인원
* 기간 : 2020.10.13 ~ 2020.12.25
* 팀원 : 한재덕, 안효재, 황동민

## 2. 사용 기술
> [requirements.txt](https://github.com/jaedeokhan/Blog-Django/blob/main/requirements.txt)
* Python 3.8
* Django 3.1.2
* Pillow Version 8.0.1 
   * Pillow는 Django models.py에서 imageField를 사용하기 위해서 설치해야한다.
   * pip install pillow Or python -m pip install pillow
* Html, Css, JQuery
* Bootstrap

## 3. ERD 설계
> [models.py](https://github.com/jaedeokhan/python-django-blog/blob/main/blogproject/blog/models.py)

![models.py](https://user-images.githubusercontent.com/45028904/110242892-65d44280-7f9b-11eb-8a10-81090a685a21.png)

## 4. 기능
1. 블로그 게시물 등록, 수정, 삭제, 리스트, 상세정보기능(CreateView, UpdateView, DeleteView, ListView, DetailView)
2. 블로그 조회수 기능(view_count)
3. 블로그 추천수 기능(likes_user)
4. 로그인, 로그아웃 기능(accounts/login, accounts/logout)

### 1. 로그인
![blog-login](https://user-images.githubusercontent.com/45028904/109371697-6741a300-78e9-11eb-8e39-c63a96f65ed3.gif)


### 2. 로그아웃
![blog-logout](https://user-images.githubusercontent.com/45028904/109371904-5b0a1580-78ea-11eb-9494-1bd61470c0c8.gif)

### 3. 블로그 게시물 리스트
![blog-list](https://user-images.githubusercontent.com/45028904/109372169-7c1f3600-78eb-11eb-99e5-1e9f2fbf2a34.gif)

### 4. 블로그 게시물 등록
![blog-regist](https://user-images.githubusercontent.com/45028904/109372264-fb146e80-78eb-11eb-9229-7652a16fdf4e.gif)

### 5. 블로그 게시물 상세보기


### 6. 블로그 게시물 수정

### 7. 블로그 게시물 삭제

### 8. 블로그 게시물 조회수 

### 9. 블로그 게시물 추천수


