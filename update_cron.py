from crontab import CronTab
from datetime import datetime


COMMAND="/home/pi/sunrise-lamp/venv/bin/python /home/pi/sunrise-lamp/light/sunrise.py"

FORMAT="%w %H %M" # format string for datetime %w is weekday by number (0 is Sun), %H is 24hr padded number and %M is the same for minutes. e.g. "1 07 30" is Monday 7:30am

def clear_cron():
    cron = CronTab(user=True)
    cron.remove_all()
    cron.write()
    is_cron_full = False
    for item in cron:
        print(item)
        is_cron_full = True

    if not is_cron_full:
        print("all cron jobs removed")


def update_cron():
    # read database for alarm times
    # delete existing crontab
    # create new crontab with updated times
    cron = CronTab(user=True)
    cron.remove_all()
    
    # temporary "database"
    # alarmtime is the time for the sunrise to complete in seconds (1800 is 30m)
    # datetime is a python datetime object/str
    database = [
        {"index": 1, "alarmtime": 1800, "datetime": "1 07 30"},  # alarm will start at 7:30 and finish at 8
        {"index": 1, "alarmtime": 1800, "datetime": "2 07 30"},  # alarm will start at 7:30 and finish at 8
        {"index": 1, "alarmtime": 1800, "datetime": "3 07 30"},  # alarm will start at 7:30 and finish at 8
        {"index": 1, "alarmtime": 1800, "datetime": "4 07 30"},  # alarm will start at 7:30 and finish at 8
        {"index": 1, "alarmtime": 1800, "datetime": "5 07 30"},  # alarm will start at 7:30 and finish at 8
    ]

    for entry in database:

        alarm = cron.new(command=COMMAND)

        alarm_time = datetime.strptime(entry["datetime"], FORMAT)

        alarm.setall(alarm_time)
        alarm.enable()

    cron.write_to_user(user=True)

    is_cron_full = False
    for item in cron:
        print(item)
        is_cron_full = True

    if not is_cron_full:
        print("no jobs in crontab")
