# -*- coding: utf-8 -*-

from datetime import datetime
import pytz

def get_date_str():
        # 设置时区为北京时间
        tz = pytz.timezone('Asia/Shanghai')
        # 获取当前日期
        now = datetime.now(tz=tz)
        # 将日期格式化为"20230324"格式
        return now.strftime('%Y%m%d')