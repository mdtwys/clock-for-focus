# clock-for-focus#
import time 

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        countdown = '{:02d}:{:02d}'.format(mins, secs)
        print(countdown, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up!')

if __name__ == '__main__':
    focus_timer(25) # 专注时长为25分钟
