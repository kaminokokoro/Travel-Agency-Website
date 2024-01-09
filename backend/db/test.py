from datetime import datetime, timedelta


time="2024-1-01 08:00:00"
time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
print(time)