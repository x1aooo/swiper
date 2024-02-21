import os

from django.conf import settings
from lib.http import rander_json
from common import error
from user.logic import send_verify_code,check_vcode
from user.models import User
from user.forms import ProfileForm


# Create your views here.

def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return rander_json(None,0)

def login(request):
    '''短信验证登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum,vcode):
        # 获取用户
        user,created = User.object.get_or_create(phonenum=phonenum)
        # 记录登录状态
        request.session['uid'] = user.id
        return rander_json(user.to_dict())
    else:
        return rander_json(None,error.VCODE_ERROR)


def get_profile(request):
    '''获取个人资料'''
    user = request.user
    return rander_json(user.profile.to_dict())
    


def modify_profile(request):
    ''''修改个人资料'''
    form = ProfileForm(request.GET)
    if form.is_valid():
        form.save()
        return rander_json(None)
    else:
        return rander_json(form.error,error.PROFILE_ERROE)


import logging
log = logging.getLevelName('inf')

def upload_avatar(request):
    ''''头像上传'''
    

    file = request.FILES.get('avatar')
    if file:
        save_upload_file(request.user,file)
        return rander_json(None)
    else:
        return rander_json(None,error.FILE_NOT_FOUND)