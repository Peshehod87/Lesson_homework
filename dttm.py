from datetime import date as dttm
from datetime import datetime as dttm1
dt = dttm(2018,5,22)
dt1 = dttm(2018,5,21)
dt2 = dttm(2018,4,22)
print(dt, '\n', dt1, '\n', dt2)
#dtstr='01/01/17'
#print(type(dtstr))
#date_dt = dttm1.strptime(dtstr, '%d/%m/%y')
#print(date_dt)
dt_str = '01/01/17 12:10:03'
#print(dt_str)
date_dt = dttm1.strptime(dt_str, '%d/%m/%y %H:%M:%S')
print(date_dt)