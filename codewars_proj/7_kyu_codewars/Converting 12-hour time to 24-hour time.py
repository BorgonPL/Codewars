def to24hourtime(hour, minute, period):
    if hour==12 : hour-=12
    return "%02d%02d" % (hour,minute) if period == 'am' else "%02d%02d" % (hour + 12,minute)
