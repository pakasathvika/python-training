'''ip:
        7262 sec
    op:
        2h:1m:2s 
    ip:
        65476
    op:
        y m w d '''


def hms(sec):
    hours = sec // 3600
    remaining_sec = sec % 3600
    minutes = remaining_sec // 60
    remaining_sec = remaining_sec % 60
    formatted_time = f"{hours}h:{minutes}m:{remaining_sec}s"
    return formatted_time

sec=int(input())
print(hms(sec))

#360days in a year, 30days in a month, 6days in a week
#360    30     6
#ip:     65476
#op: ?y   ?m   ?w   ?d


n=int(input())
y=n//360
n=n%360
m=n//30
n=n%30
w=n//6
d=n%6
print(f"{y}:{m}:{w}:{d}")