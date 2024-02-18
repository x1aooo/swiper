from django.htto import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import rander_json
from common import error

class AuthMiddleware(MiddlewareMixin):
    '''用户登录验证中间件'''
    WHITE_list = [
        '/api/user/verify',
        'api/user/login'
    ]
    def process_request(self,request):
        # 如果请求的URL在白名单内，直接跳过检查
        for path in self.WHITE_list:
            if request.path.startwith(path):
                return

        # 进行登录检查
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.object.get(id=uid)
                return 
            except User.DoesNotExist:
                request.session.flush()
        return rander_json(None,code = error.LOGIN_ERROR)

class CorsMiddleware(MiddlewareMixin):
    ''''处理客JS户端的跨越'''
    def process_request(self,request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Content-Length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META
            ['HTTP_ACCESS_CONTROL_REQUEST_METHOD']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
            return response

    def process_request(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response