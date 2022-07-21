from lcd1602 import*
import datetime
import threading

def get_curr_year(curr_datetime):
    return curr_datetime.strftime("%y")
def get_curr_month(curr_datetime):
    return curr_datetime.strftime("%m")
def get_curr_day(curr_datetime):
    return curr_datetime.strftime("%d")
def get_curr_h(curr_datetime):
    return curr_datetime.strftime("%H")
def get_curr_m(curr_datetime):
    return curr_datetime.strftime("%M")
def get_curr_s(curr_datetime):
    return curr_datetime.strftime("%S")

def get_time_diff(day_diff,curr_datetime, due_time):
    curr_h = int(get_curr_h(curr_datetime))
    curr_m = int(get_curr_m(curr_datetime))
    curr_s = int(get_curr_s(curr_datetime))
    due_time = due_time.split(":")
    due_h, due_m, due_s = int(due_time[0]), int(due_time[1]), int(due_time[2])
    if day_diff == 0:
        return str(due_h - curr_h) + ":" + str(due_m - curr_m) + ":" + str(due_s - curr_s)
    else:
        return str(23 - curr_h) + ":" + str(59 - curr_m) + ":" + str(59 - curr_s)

def get_day_diff(due_datetime, curr_datetime):
    day_diff = due_datetime - curr_datetime
    day_diff = day_diff.days
    return day_diff

def line1(lcd):
    text = "To 25/08/2022 14:45:00 "
    length = lcd.lcd_line_width
    head = 0
    while head < length:
        loop_text = (head+length) % length
        real_text = text[head:head+length] + text[:loop_text]
        lcd.lcd_text(real_text, 1)
        head += 1
        for x in range(30):
            line2(lcd)
def line2(lcd):
    due_datetime = datetime.datetime(day=25, month=8, year=2022)
    due_time = "14:45:00"
    curr_datetime = datetime.datetime.now()
    #curr_date = curr_datetime.strftime("%d/%m/%y")
    day_diff = get_day_diff(due_datetime, curr_datetime)
    time_diff = get_time_diff(day_diff, curr_datetime, due_time)
    lcd.lcd_text(str(day_diff) + "days " + str(time_diff), 2)
    
try:
    lcd = lcd1602()
    while True:
        #thread1 = threading.Thread(target=line1, args=(lcd,))
        #thread2 = threading.Thread(target=line2, args=(lcd,))
        #thread1.start()
        #thread2.start()
        line1(lcd)
        #line2(lcd)

except KeyboardInterrupt:
    pass
finally:
    lcd = lcd1602()
    lcd.lcd_write_cmd(0x01)
    GPIO.cleanup()
