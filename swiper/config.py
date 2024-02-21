'''
第三方配置
'''


# 互亿无限短信配置
HY_SMS_URL = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account':'C19801954',
    'password':'25d8d165ae313713b1c0cde657c5f25f',
    'content':'您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile':None,
    'format':'json'
}


# 七牛配置
QN_ACCESS_KEY = 'U2jEKYQ-o7ApnKTucp3a8ApRlMYBReliQjyn9gxE'
QN_SECRET_KEY = 'UXis_d3jiMTHEcVSmNyLRLzwt1Xu0kC588bTuag3'
QN_BUCKET_NAME = 'swiper-bjc'
QN_BASE_URL = 's9540xq1d.hd-bkt.clouddn.com'