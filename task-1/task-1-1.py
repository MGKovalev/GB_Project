duration = int(input("vvedite kol-vo sekund: "))
print(duration)
##print (60 * 60 * 24)

# 86400 - day
# 3600 - hour

if duration >= 86400:
    day = duration // 86400
    hour = (duration - (86400 * day)) // 3600
    min = (duration - (86400 * day) - (3600 * hour)) // 60
    sec = duration - (86400 * day) - (3600 * hour) - (60 * min)
    print("day: ", day, " hour: ", hour, " min: ", min, " sec: ", sec)
elif duration < 86400 and duration >= 3600:
    hour = duration // 3600
    min = (duration - (3600 * hour)) // 60
    sec = duration - (3600 * hour) - (60 * min)
    print( " hour: ", hour, " min: ", min, " sec: ", sec)
elif duration < 3600 and duration >= 60:
    min = duration // 60
    sec = duration - (60 * min)
    print( " min: ", min, " sec: ", sec)
else:
    sec = duration
    print ( " sec: ", sec )

