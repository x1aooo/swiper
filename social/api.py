from lib.http import rander_json

from social import logic
from social.models import Friend

# Create your views here.

def get_users(request):
    '''获取推荐列表'''
    group_num = int(request.GET.get('group_num',0))
    start = group_num * 5
    end = start + 5
    users = logic.get_rcmd_users(request.user)[start:end]

    result = [user.to_dict() for user in users]
    return rander_json()

def like(request):
    '''喜欢'''
    sid = request.POST.get('id')
    is_matched = logic.like(request.user,sid)
    return rander_json({'is_matched':is_matched})

def superlike(request):
    '''超级喜欢'''
    sid = request.POST.get('id')
    is_matched = logic.superlike(request.user,sid)
    return rander_json({'is_matched':is_matched})

def dislike(request):
    '''不喜欢'''
    sid = request.POST.get('id')
    logic.dislike(request.user,sid)
    return rander_json(None)

def rewind(request):
    '''后悔'''
    sid = request.POST.get('id')
    logic.rewind(request.user,sid)
    return rander_json(None)

def friends(request):
    '''好友列表'''
    my_friends = Friend.friends(request.user.id)
    friends_info =[frd.to_dict() for frd in my_friends]
    return rander_json({'friedns':friends_info})