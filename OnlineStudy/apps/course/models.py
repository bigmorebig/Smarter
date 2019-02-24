from datetime import datetime

from django.db import models
# Create your models here.
from organization.models import CourseOrg,Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name='课程机构',null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name='课程名')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',null=True,blank=True,on_delete=models.CASCADE)
    degree = models.CharField(verbose_name='难度',choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name='学习时长(分钟数)')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m',verbose_name='封面图',max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    categroy = models.CharField(default='后端开发',max_length=20,verbose_name='课程类别')
    tag = models.CharField(default='',verbose_name='课程标签',max_length=10)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    need_know = models.CharField(default='',max_length=300,verbose_name='课程须知')
    teacher_tell = models.CharField(default='',max_length=500,verbose_name='老师告诉你能学到什么?')
    course_notice = models.CharField(default='',max_length=500,verbose_name='课程公告')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        '''获取课程章节数'''
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        '''获取课程所有章节'''
        return self.lesson_set.all().all()



class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name='章节名')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        '''获取章节视频'''
        return  self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='视频名')
    url = models.CharField(max_length=200,verbose_name='访问地址',default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    # 文件类型FileField，在后台管理系统中会直接有上传的按钮，FileField本质上是字符串类型，要指定最大长度
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件", max_length=100)
    add_time = models.DateTimeField(auto_now_add=True,  verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
