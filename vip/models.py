'''
Vip - User:一对多
Vip - Permission：多对多
'''

from django.db import models


class Vip(models.Model):
    name = models.CharField(max_length=32,unique=True)
    level = models.IntegerField()
    price = models.FloatField()
    
    def perms(self):
        '''当前Vip具有的权限'''
        relations = VipPermRelation.objects.filter(vip_id=self.id)
        perm_id_list = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id_list)
    
    def had_perm(self,perm_name):
        '''检查是否具有某种权限'''
        perm = Permission.objects.get(name=perm_name)
        return VipPermRelation.objects.filter(vip_id=self.id,perm_id=perm.id).exists()

class Permission(models.Model):
    '''
    权限表
        vipflak      会员身份标识
        superlike    超级喜欢
        rewind       后悔功能
        anylocation  任意更改定位
        unlimit_like 无限次数喜欢
    '''
    name = models.CharField(max_length=32,unique=True)

class VipPermRelation(models.Model):
    '''
    会员-权限 关系表

        会员套餐1
            会员身份标识
            超级喜欢
        会员套餐2
            会员身份标识
            反悔功能
        会员套餐3
            会员身份标识
            超级喜欢
            反悔功能
            任意更改定位
            无限喜欢次数
    '''
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()
