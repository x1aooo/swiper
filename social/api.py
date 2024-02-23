from lib.http import rander_json

from social.logic import get_rcmd_users

# Create your views here.

def get_users(request):
    '''获取推荐列表'''
    group_num = int(request.GET.get('group_num',0))
    start = group_num * 5
    end = start + 5
    users = get_rcmd_users(request.user)[start:end]

    result = [user.to_dict() for user in users]
    return rander_json()

def like(request):
    '''喜欢'''
    
    return rander_json()

def superlike(request):
    '''超级喜欢'''
    return rander_json()

def dislike(request):
    '''不喜欢'''
    return rander_json()

def rewind(request):
    '''后悔'''
    return rander_json()
