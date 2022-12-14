from datetime import datetime, time, timedelta
def classes(time_string):
    if datetime.now().weekday() == 6:
        print("Today is sunday")
        return
    cur_date = datetime.now().date()
    hh, mm, ss =(int(s) for s in time_string.split(":"))
    t= datetime(cur_date.year, cur_date.month , cur_date.day , hh, mm, ss)
    timetable = [datetime(cur_date.year, cur_date.month , cur_date.day,9,30, 0), 
    datetime(cur_date.year, cur_date.month , cur_date.day,11, 15, 0), 
    datetime(cur_date.year, cur_date.month , cur_date.day,13, 40, 0), 
    datetime(cur_date.year, cur_date.month , cur_date.day,15, 25, 0), 
    datetime(cur_date.year, cur_date.month , cur_date.day,17, 10, 0)]
    i =-1
    for u_class in timetable:
        if t < u_class:
            break
        i+=1
    if i == -1:
        print("Classes have not started yet")
        return
    delta =t - timetable[i]
    class_length = timedelta(hours=1,minutes= 35,seconds= 0)
    if delta>class_length:
        if i==4:
            print("Classes are over!")
            return
        print("Break time!")
        return
    print(class_length - delta)

#classes("15:15:01")
#classes("7:15:01")
classes(datetime.now().strftime("%H:%M:%S"))