import time
print(time.strftime("%d-%a-%Y")) #현재 날짜를 일-요일-연도

import datetime
# p는 parse 즉 날짜 해석
dt=datetime.datetime.strptime("2022-12-1","%Y-%m-%d")
print(type(dt))
# 위의 지정 날짜를 포멧에 맞춰 출력
print(dt.strftime("%d-%a-%Y"))