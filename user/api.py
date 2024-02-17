from lib.http import rander_json
from user.logic import send_verify_code

# Create your views here.

def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return rander_json(None,0)

def login(request):
    '''短信验证登录'''
    cache.get(key)


def get_profile(request):
    '''获取个人资料'''


def modify_profile(request):
    ''''修改个人资料'''


def upload_avatar(request):
    ''''头像上传'''