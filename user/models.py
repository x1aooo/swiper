import datetime
from django.db import models
from django.utils.functional import cached_property

# Create your models here.

class User(models.Model):
    '''用户数据模型'''

    SEX = (
        ('男','男'),
        ('女','女'),
    )
    nickname = models.CharField(max_length=32,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)

    sex = models.CharField(max_length=8,choices=SEX)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)

    @cached_property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        times = today - birth_date
        return times.days // 365
    
    @property
    def profile(self):
        '''用户的配置项'''
        if not hasattr(self,'_profile'):
            self._profile,_ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    '''用户配置项'''
    
    SEX = (
        ('男','男'),
        ('女','女'),
    )
    dating_sex = models.CharField(default='女',max_length=8,choices=SEX,verbose_name='性别的匹配')
    location = models.CharField(max_length=32,verbose_name='目标城市')
    
    min_distance = models.IntegerField(default=1,verbose_name='最小查找目标')
    max_distance = models.IntegerField(default=10,verbose_name='最大查找目标')

    min_dating_age = models.IntegerField(default=18,verbose_name='最小交友范围')
    max_dating_age = models.IntegerField(default=45,verbose_name='最大交友范围')

    vibration = models.BooleanField(default=True,verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True,verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True,verbose_name='是否自动播放视频')