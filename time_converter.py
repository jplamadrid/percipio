from datetime import datetime
### Convert 12 Hour time to 24 Hour Time
m2 = '5:00 PM'
in_time = datetime.strptime(m2, "%I:%M %p")
out_time = datetime.strftime(in_time, "%H:%M")
print(out_time)
