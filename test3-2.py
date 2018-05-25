import datetime
 
 
today = datetime.datetime.today()
 
# 今日の日付
print(today)
 
# 明日の日付
print(today + datetime.timedelta(days=1))
 
newyear = datetime.datetime(2018, 1, 1)
 
# 2018年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))
 
# 2018年1月1日から今日までの日数
calc = today - newyear
 
# 計算結果の戻り値は「timedelta」
print(calc.days)