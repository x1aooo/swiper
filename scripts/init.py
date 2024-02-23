#! /bin/bash python

import os
import sys
import random

import django

# 设置环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","swiper.settings")
django.setup()

from user.models import User

last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨',
    '朱秦尤许何吕施张孔曹严华金魏陶姜',
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎',
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐',
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常',
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    '男':[
        '洛冰','奕启','钧心','辛皓','亦骏',
        '皓煜','鹭洋','叶轩','南弦','莫羡',
        '振博','御嘉','无洛','睿磊','玉堂',
        '琦宁','鸿皓','盛冰','翊颢','轩学',
        '丘黎','皓阳','景禹','钧枫','浩灿'
    ],
    '女':[
        '露怡','琦倩','澜蕾','思琳','新梵',
        '莺颖','桃婉','芙晴','艺凝','瑾桦',
        '姬熙','叶雅','洋露','梵芙','娇瑾',
        '慕滢','琼嘉','云新','荷怡','纤滢',
        '涵欢','芙秀','丹媚','语毓','可缨'
    ]
}

def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name,first_name]),sex

# 创建初始用户
for i in range(1000):
    name,sex = random_name()
    try:
        User.objects.create(
            phonenum = '%s' % random.randrange(21000000000,21900000000),
            nickname = name,
            sex = sex,
            birth_year = random.randint(1980,2000),
            birth_month = random.randint(1,12),
            birth_day = random.randint(1,28),
            location = random.choice(['北京','上海','深圳','成都','沈阳','西安','武汉']) 
        )
    except django.db.utils.IntegrityError:
        pass